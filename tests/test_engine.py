"""Tests for the parser seam, registry routing, and deterministic stages.

These pin the contract the architecture rests on: fallback chains, force/compare
modes, image→vision routing, Mermaid validation, and token optimisation.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure the in-repo package is importable without installing.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from doc2md.mermaid_validate import clean_llm_mermaid  # noqa: E402
from doc2md.optimise import optimise  # noqa: E402
from doc2md.parsers.base import ExtractionResult  # noqa: E402
from doc2md.parsers.registry import ExtractorRegistry  # noqa: E402


# -- fake parsers --------------------------------------------------------

class _FakeParser:
    def __init__(self, name, text, *, avail=True, exts=(".pdf",)):
        self.name = name
        self._text = text
        self._avail = avail
        self.extensions = exts
        self.kinds = ("file",)

    @property
    def available(self):
        return self._avail

    def supports(self, source):
        return Path(source).suffix.lower() in self.extensions

    def extract(self, source, *, ocr=False):
        return ExtractionResult(text=self._text, parser=self.name)


def _registry(*parsers):
    return ExtractorRegistry(parsers, chains={".pdf": [p.name for p in parsers]})


# -- registry: fallback chain -------------------------------------------

def test_fallback_chain_first_wins():
    reg = _registry(_FakeParser("a", "hello"), _FakeParser("b", "world"))
    r = reg.extract("x.pdf")
    assert r.parser == "a"
    assert r.used_fallback is False
    assert r.text == "hello"


def test_fallback_chain_skips_empty():
    reg = _registry(_FakeParser("a", ""), _FakeParser("b", "world"))
    r = reg.extract("x.pdf")
    assert r.parser == "b"
    assert r.used_fallback is True
    assert r.text == "world"


def test_fallback_chain_unavailable_skipped():
    reg = _registry(_FakeParser("a", "", avail=False), _FakeParser("b", "ok"))
    r = reg.extract("x.pdf")
    assert r.parser == "b"
    assert r.ok


def test_force_parser():
    reg = _registry(_FakeParser("a", "first"), _FakeParser("b", "second"))
    r = reg.extract("x.pdf", parser="b")
    assert r.parser == "b"
    assert r.text == "second"


def test_force_unknown_parser_yields_empty():
    reg = _registry(_FakeParser("a", "first"))
    r = reg.extract("x.pdf", parser="nope")
    assert not r.ok


def test_compare_runs_all_available():
    reg = _registry(_FakeParser("a", "A"), _FakeParser("b", "B", avail=False), _FakeParser("c", "C"))
    results = reg.extract_all("x.pdf")
    assert [x.parser for x in results] == ["a", "c"]


# -- image parser routes to vision --------------------------------------

def test_image_parser_flags_vision():
    from doc2md.parsers.image import ImageParser

    p = ImageParser()
    # patch OCR away to keep it deterministic / binary-free
    r = p.extract(str(ROOT / "tests" / "_does_not_exist.png"), ocr=False)
    assert r.meta.get("needs_vision") is True
    assert r.images  # the source path is carried for vision


# -- mermaid validation --------------------------------------------------

def test_clean_llm_mermaid_strips_fence_and_validates():
    raw = "```mermaid\nflowchart TD\nA-->B\n```"
    src, reason = clean_llm_mermaid(raw)
    assert src is not None
    assert src.startswith("flowchart TD")


def test_clean_llm_mermaid_rejects_bad_head():
    src, reason = clean_llm_mermaid("notamermaid\nA-->B")
    assert src is None


def test_clean_llm_mermaid_rejects_unbalanced():
    src, reason = clean_llm_mermaid("classDiagram\nClassX {\nint id")
    assert src is None
    assert "brace" in reason


# -- token optimisation --------------------------------------------------

def test_optimise_strips_page_markers_and_collapses_blanks():
    pages = []
    for i in range(1, 7):
        pages.append(f"<!-- page {i} -->\nRunning Header Co.\nbody {i}")
    text = "\n\n".join(pages) + "\n"
    out = optimise(text)
    assert "<!-- page" not in out
    assert "Running Header Co." not in out  # repeated 6x → running header removed
    assert "\n\n\n" not in out
    assert "body 1" in out and "body 6" in out


def test_optimise_preserves_real_short_lines():
    out = optimise("Intro\n\nSome unique content here\n")
    assert "Intro" in out
    assert "Some unique content here" in out


# -- external binary parsers (pdf-inspector, undoc, unpdf) ------------

def test_external_parsers_registered_and_routed():
    from doc2md.parsers import build_registry

    reg = build_registry()
    for name in ("pdf-inspector", "undoc", "unpdf"):
        assert name in reg.parsers, f"{name} not registered"

    assert reg.parsers["pdf-inspector"].supports("x.pdf")
    assert reg.parsers["unpdf"].supports("x.pdf")
    assert reg.parsers["undoc"].supports("x.docx")
    assert reg.parsers["undoc"].supports("x.pptx")
    assert not reg.parsers["undoc"].supports("x.pdf")  # undoc does not do PDF

    # chains put the Rust parsers first; unavailable ones skip silently.
    assert reg.chains[".pdf"][0] == "pdf-inspector"
    assert reg.chains[".docx"][0] == "undoc"


def test_external_parser_cli_args():
    from doc2md.parsers.pdf_inspector import PdfInspectorParser
    from doc2md.parsers.undoc import UndocParser
    from doc2md.parsers.unpdf import UnpdfParser

    assert PdfInspectorParser().binary == "pdf2md"
    assert PdfInspectorParser().args("doc.pdf", ocr=False) == ["doc.pdf"]
    assert UndocParser().binary == "undoc"
    assert UndocParser().args("doc.docx", ocr=False) == ["markdown", "doc.docx"]
    assert UnpdfParser().binary == "unpdf"
    assert UnpdfParser().args("doc.pdf", ocr=False) == ["markdown", "doc.pdf"]


# -- work-item id uniqueness + cache reuse + mark_done ------------------

def _fake_parser_factory(text):
    """Build a fake parser that returns the given text for any source."""
    class _P:
        name = "fake"
        kinds = ("file",)
        extensions = (".md",)

        @property
        def available(self):
            return True

        def supports(self, source):
            return Path(source).suffix.lower() in self.extensions

        def extract(self, source, *, ocr=False):
            return ExtractionResult(text=text, parser=self.name)

    return _P()


def test_work_item_ids_unique_across_images_and_pages(tmp_path):
    """Two infographic sources must not collide on item id (was f{hash[:8]}-img)."""
    from doc2md.engine import Engine

    raw = tmp_path / "raw"
    raw.mkdir()
    (raw / "a.md").write_text("body text")
    cache = tmp_path / "cache"
    src = tmp_path / "sources"

    class _TwoImage:
        name = "twoimg"
        kinds = ("file",)
        extensions = (".md",)

        @property
        def available(self):
            return True

        def supports(self, source):
            return Path(source).suffix.lower() == ".md"

        def extract(self, source, *, ocr=False):
            return ExtractionResult(
                text="body", parser=self.name,
                images=["img1.png", "img2.png"],
                meta={"needs_vision": True},
            )

    reg = ExtractorRegistry([_TwoImage()], chains={".md": ["twoimg"]})
    eng = Engine(raw, src, cache, registry=reg, ocr=False)
    report = eng.convert_one(raw / "a.md")
    ids = [i["id"] for i in report.items]
    assert len(ids) == len(set(ids)), f"ids not unique: {ids}"
    assert len(ids) == 2


def test_extraction_cache_reused_on_rerun(tmp_path):
    """A second convert_one must reuse the cached extraction (no parser re-run)."""
    from doc2md.engine import Engine

    raw = tmp_path / "raw"
    raw.mkdir()
    (raw / "a.md").write_text("hello world")
    calls = {"n": 0}

    class _Counting:
        name = "count"
        kinds = ("file",)
        extensions = (".md",)

        @property
        def available(self):
            return True

        def supports(self, source):
            return Path(source).suffix.lower() == ".md"

        def extract(self, source, *, ocr=False):
            calls["n"] += 1
            return ExtractionResult(text=f"v{calls['n']}", parser=self.name)

    reg = ExtractorRegistry([_Counting()], chains={".md": ["count"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", registry=reg, ocr=False, parser="count")
    r1 = eng.convert_one(raw / "a.md")
    assert r1.parser == "count"
    r2 = eng.convert_one(raw / "a.md")
    # Forced parser skips the skip-path, so the second run reaches _extract and
    # hits the extraction cache → no second extract call.
    assert calls["n"] == 1
    assert "v1" in Path(r1.source).read_text()


def test_mark_done_clears_needs_llm(tmp_path):
    """apply_work clears needs_llm once no await markers remain."""
    from doc2md.engine import Engine

    raw = tmp_path / "raw"
    raw.mkdir()
    (raw / "a.md").write_text("body text")

    class _Complex:
        name = "cx"
        kinds = ("file",)
        extensions = (".md",)

        @property
        def available(self):
            return True

        def supports(self, source):
            return Path(source).suffix.lower() == ".md"

        def extract(self, source, *, ocr=False):
            # Text that triggers complex detection (parallel + many components).
            return ExtractionResult(text="parallel async fork join\n" + " ".join(
                f"Comp{i}Item" for i in range(25)), parser=self.name)

    reg = ExtractorRegistry([_Complex()], chains={".md": ["cx"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", registry=reg, ocr=False)
    r1 = eng.convert_one(raw / "a.md")
    assert r1.needs_llm
    item_id = r1.items[0]["id"]
    eng.apply_work(r1.source, {item_id: "```mermaid\nflowchart TD\nA-->B\n```"})
    r2 = eng.convert_one(raw / "a.md")
    assert not r2.needs_llm
    assert r2.skipped


def test_work_cache_skips_llm_on_rerun(tmp_path):
    """A previously-fulfilled item is inlined from cache → needs_llm False."""
    from doc2md.engine import Engine

    raw = tmp_path / "raw"
    raw.mkdir()
    (raw / "a.md").write_text("parallel async fork join " + " ".join(
        f"Comp{i}Item" for i in range(25)))

    class _CX:
        name = "cx"
        kinds = ("file",)
        extensions = (".md",)

        @property
        def available(self):
            return True

        def supports(self, source):
            return Path(source).suffix.lower() == ".md"

        def extract(self, source, *, ocr=False):
            return ExtractionResult(text=open(source).read(), parser=self.name)

    reg = ExtractorRegistry([_CX()], chains={".md": ["cx"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", registry=reg, ocr=False, parser="cx")
    r1 = eng.convert_one(raw / "a.md")
    item_id = r1.items[0]["id"]
    mermaid = "```mermaid\nflowchart TD\nA-->B\n```"
    eng.apply_work(r1.source, {item_id: mermaid})
    # Second run with forced parser does NOT skip, so it reaches _extract and
    # pre-fulfils the complex item from the work cache → needs_llm False.
    r2 = eng.convert_one(raw / "a.md")
    assert not r2.needs_llm
    assert not r2.skipped


# -- mermaid validation: subgraph/end + erDiagram exemption --------------

def test_validate_rejects_unbalanced_subgraph_end():
    src, reason = clean_llm_mermaid("flowchart TD\nsubgraph A\nA-->B")
    assert src is None
    assert "subgraph" in reason


def test_validate_erdiagram_exempt_from_brace_check():
    # erDiagram with unbalanced braces (partial attribute block) is accepted.
    src, reason = clean_llm_mermaid("erDiagram\nCustomer ||--o{ Order")
    assert src is not None, reason


# -- optimise: bare page-number-only lines ------------------------------

def test_optimise_keeps_bare_numeric_lines():
    # A line that is just "42" is NOT a page number — must be preserved.
    out = optimise("Some heading\n\n42\n\nmore text\n")
    assert "\n42\n" in out


def test_optimise_strips_page_n_of_m():
    out = optimise("body one\n\n3 of 10\n\nbody two\n")
    assert "3 of 10" not in out


# -- detection: component_count regex ---------------------------------

def test_detection_component_count_ignores_plain_words():
    from doc2md.detection import detect_diagrams

    # "The And It First" are plain capitalised words, not components.
    d = detect_diagrams("The cat sat. And it ran. First one then two.")
    assert d.component_count == 0


def test_detection_component_count_catches_camelcase():
    from doc2md.detection import detect_diagrams

    d = detect_diagrams("AuthService calls UserDB and the API via order_id")
    assert d.component_count >= 3


# -- detection generalisation (R1-R5): pin classes, not one doc -----------

def test_detection_component_count_is_distinct():
    """A repeated acronym counts once, not 200× (R1)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams("TDS deducted. TDS deposited. TDS TDS TDS. HDFC HDFC.")
    # Two distinct components: TDS, HDFC — not 5.
    assert d.component_count == 2


def test_detection_table_with_acronyms_is_none():
    """A table of 'Status: Active' rows + repeated ALL-CAPS codes has words but
    no edges → not a diagram (R2). This is the AIS false-positive class."""
    from doc2md.detection import detect_diagrams

    table = (
        "Salary\n"
        "SR.NO TDS-192 Salary received SITA LIMITED COUNT 6 AMOUNT 3565240 STATUS Active\n"
        "1 Q2 30/09/2025 1073754 0 0 Active\n"
        "2 Q2 31/08/2025 375090 81999 81999 Active\n"
        "Dividend\n"
        "SR.NO TDS-194 Dividend received TATA LIMITED COUNT 4 AMOUNT 285580 STATUS Active\n"
        "1 Q4 17/01/2026 149340 14934 14934 Active\n"
    )
    d = detect_diagrams(table)
    assert d.complexity == "none", d.reasons
    assert d.has_diagram is False


def test_detection_prose_with_acronyms_is_none():
    """Prose mentioning many acronyms but no relationships → none (R2)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams(
        "The TDS and SFT regimes interact with PAN and HDFC. "
        "The ECS and TCS systems report to AMC. BSR codes apply."
    )
    assert d.complexity == "none"


def test_detection_step_sequence_is_simple():
    """First/Then/Next steps form a linear process diagram → simple (R2)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams(
        "First we receive the order.\n"
        "Then we validate the payment.\n"
        "Next we ship the package.\n"
        "Finally we send the receipt.\n"
    )
    assert d.has_diagram is True
    assert d.complexity == "simple"


def test_detection_edges_only_defaults_to_flowchart():
    """A diagram established by edges, with no keyword hits, types as flowchart (R5)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams("Order -> Payment -> Ship -> Receipt")
    assert d.has_diagram is True
    assert d.diagram_type == "flowchart"


def test_detection_real_architecture_is_complex():
    """Edges + many distinct components + branching → complex (R2 degree)."""
    from doc2md.detection import detect_diagrams

    text = (
        "AuthService -> UserDB -> APIClient\n"
        + " ".join(f"Comp{i}Svc" for i in range(25))
        + "\nif token valid then grant else deny"
    )
    d = detect_diagrams(text)
    assert d.complexity == "complex"
    assert d.has_diagram is True


def test_detection_keyword_word_boundary_state_not_statement():
    """'state' must not match 'statement'; 'flow' must not match 'flower' (R3)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams("The statement of account lists flowers for the estate.")
    # 'state' is a keyword but should not fire on statement/estate;
    # 'flow'/'process'/'status'/etc. absent → no diagram.
    assert "state" not in d.keywords_found
    assert d.complexity == "none"


def test_detection_keyword_suffix_matches_inflections():
    """'class' matches 'classes'; 'send' matches 'sends' (R3 light suffix)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams("The classes extend each other. sends request -> response")
    # 'class' keyword should match 'classes'; the arrow gives edges → diagram.
    assert "class" in d.keywords_found


# -- detection: relational-verb prose (closed recall gap) ----------------

def test_detection_class_hierarchy_from_prose_is_complex():
    """A class hierarchy stated in prose (no arrows) → complex, routed to
    Claude (the deterministic generator can't render class diagrams)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams(
        "AuthService extends BaseAuthService. "
        "OrderService implements IOrder. "
        "PaymentService implements IPayment."
    )
    assert d.has_diagram is True
    assert d.complexity == "complex", d.reasons
    assert d.diagram_type == "class"


def test_detection_er_references_from_prose_is_complex():
    """ER relationships stated in prose → complex (deterministic can't render ER)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams(
        "Order references Customer. Product references Category. Invoice references Order."
    )
    assert d.has_diagram is True
    assert d.complexity == "complex", d.reasons
    assert d.diagram_type == "er"


def test_detection_dependency_from_prose_is_complex():
    """A dependency graph stated in prose → complex (no deterministic renderer)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams(
        "AuthService depends on APIClient. DBService depends on AuthService."
    )
    assert d.has_diagram is True
    assert d.complexity == "complex", d.reasons


def test_detection_minimal_two_relationships_is_diagram():
    """Two relational verbs are enough to establish a diagram (gap closure)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams("Foo extends Bar. Baz implements Qux.")
    assert d.has_diagram is True
    assert d.complexity == "complex"


def test_detection_relational_precision_lowercase_prose_is_none():
    """Relational verbs with lowercase operands (common prose) must NOT fire —
    the capitalized-operand constraint keeps precision (R2)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams(
        "the report extends the analysis. "
        "the system depends on the config. "
        "this module is part of the larger framework."
    )
    assert d.complexity == "none", d.reasons
    assert d.has_diagram is False


def test_detection_single_titlecase_relation_is_none():
    """A single title-case relational verb is not enough — need >=2 (precision)."""
    from doc2md.detection import detect_diagrams

    d = detect_diagrams("Report extends Analysis. Otherwise unrelated prose.")
    assert d.has_diagram is False
    assert d.complexity == "none"


# -- optimise: strikethrough garbage stripping (R4) ----------------------

def test_optimise_strips_strikethrough_garbage():
    out = optimise("body text\n\n~~QO~~ ~~a eee~~ ~~GQ~~\n\nmore text\n")
    assert "~~" not in out
    assert "body text" in out
    assert "more text" in out


def test_optimise_strikethrough_does_not_merge_words():
    """Striking deletes the struck text but must not merge the neighbours into a
    false CamelCase token (R4 safety): ``Annual~~Info~~Statement`` →
    ``Annual Statement``, never ``AnnualStatement``."""
    out = optimise("Annual~~Info~~Statement report\n")
    assert "AnnualStatement" not in out  # neighbours not merged
    assert "Annual Statement" in out


# -- figure-page → vision routing (option 2) -----------------------------

def test_figures_has_picture_omission():
    from doc2md.figures import has_picture_omission

    assert has_picture_omission("**==> picture [889 x 438] intentionally omitted <==**")
    assert not has_picture_omission("A normal paragraph with no figure.")


def test_figures_picture_omitted_pages():
    from doc2md.figures import picture_omitted_pages

    page_texts = {
        1: "page one, no figure",
        2: "intro\n**==> picture [8x8] intentionally omitted <==**\nfig labels",
        3: "page three, also none",
    }
    assert picture_omitted_pages(page_texts) == [2]


def test_figures_strip_picture_markers_keeps_figure_text():
    from doc2md.figures import strip_picture_markers

    text = (
        "intro\n"
        "**==> picture [889 x 438] intentionally omitted <==**\n"
        "**----- Start of picture text -----**\n"
        "BAGERA Global View — real figure labels here\n"
        "**----- End of picture text -----**\n"
        "outro\n"
    )
    out = strip_picture_markers(text)
    assert "intentionally omitted" not in out
    assert "Start of picture text" not in out
    assert "End of picture text" not in out
    assert "real figure labels here" in out  # figure text preserved
    assert "intro" in out and "outro" in out


def test_optimise_strips_picture_annotation_lines():
    out = optimise(
        "Some intro text\n\n"
        "**==> picture [889 x 438] intentionally omitted <==**\n"
        "**----- Start of picture text -----**\n"
        "figure labels\n"
        "**----- End of picture text -----**\n\n"
        "outro\n"
    )
    assert "intentionally omitted" not in out
    assert "Start of picture text" not in out
    assert "figure labels" in out


def test_optimise_strips_picture_annotation_with_trailing_br():
    """pymupdf4llm sometimes appends ``<br>`` to the annotation lines."""
    out = optimise(
        "intro\n"
        "**==> picture [8x8] intentionally omitted <==**<br>\n"
        "**----- Start of picture text -----**<br>\n"
        "labels<br>\n"
        "**----- End of picture text -----**<br>\n"
        "outro\n"
    )
    assert "intentionally omitted" not in out
    assert "Start of picture text" not in out
    assert "End of picture text" not in out
    assert "labels" in out


def test_pymupdf4llm_emits_vision_pages_for_picture():
    """The parser maps picture-omission markers to 1-based vision_pages,
    without requiring the real pymupdf4llm binary."""
    import sys
    import types

    fake = types.ModuleType("pymupdf4llm")

    def to_markdown(source, page_chunks=False):
        if not page_chunks:
            return "plain text"
        return [
            {"metadata": {"page_number": 1}, "text": "page one, no figure"},
            {"metadata": {"page_number": 2},
             "text": "intro\n**==> picture [8x8] intentionally omitted <==**\nfig labels"},
            {"metadata": {"page_number": 3}, "text": "page three"},
        ]

    fake.to_markdown = to_markdown
    orig = sys.modules.get("pymupdf4llm")
    sys.modules["pymupdf4llm"] = fake
    try:
        from doc2md.parsers.pymupdf4llm import Pymupdf4llmParser
        r = Pymupdf4llmParser().extract("x.pdf")
        assert r.ok
        assert r.meta.get("vision_pages") == [2]
        assert "page one" in r.text and "page three" in r.text
    finally:
        if orig is not None:
            sys.modules["pymupdf4llm"] = orig
        else:
            sys.modules.pop("pymupdf4llm", None)