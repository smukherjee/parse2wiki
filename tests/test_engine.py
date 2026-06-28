"""Tests for the parser seam, registry routing, and deterministic stages.

These pin the contract the architecture rests on: fallback chains, force/compare
modes, image→vision routing, Mermaid validation, and token optimisation.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

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


# -- graphic_dense_pages: visual diagram detection via pdfplumber ----------

def _fake_plumber_with_pages(pages_spec: list[dict]):
    """Build a fake pdfplumber module whose PDF has one page per spec dict.

    Each spec may contain: rects (list of dicts), lines (list), curves (list).
    """
    import sys, types

    fake = types.ModuleType("pdfplumber")

    class _FakePage:
        def __init__(self, spec):
            self.rects = spec.get("rects", [])
            self.lines = spec.get("lines", [])
            self.curves = spec.get("curves", [])

    class _FakePDF:
        def __init__(self, specs):
            self.pages = [_FakePage(s) for s in specs]

        def __enter__(self):
            return self

        def __exit__(self, *a):
            pass

    fake.open = lambda source: _FakePDF(pages_spec)
    return fake


def _with_fake_plumber(pages_spec, fn):
    import sys

    fake = _fake_plumber_with_pages(pages_spec)
    orig = sys.modules.get("pdfplumber")
    sys.modules["pdfplumber"] = fake
    try:
        return fn()
    finally:
        if orig is not None:
            sys.modules["pdfplumber"] = orig
        else:
            sys.modules.pop("pdfplumber", None)


def _rect(w, h):
    return {"width": w, "height": h}


def test_graphic_dense_pages_flags_diagram_page():
    """A page with 6 big rects + 12 lines is flagged as a figure page."""
    from doc2md.figures import graphic_dense_pages

    spec = [{"rects": [_rect(100, 80)] * 6, "lines": [{}] * 12, "curves": []}]
    result = _with_fake_plumber(spec, lambda: graphic_dense_pages("any.pdf"))
    assert result == [1]


def test_graphic_dense_pages_ignores_sparse_graphics():
    """A page with only 2 rects and 5 lines is below both thresholds → not flagged."""
    from doc2md.figures import graphic_dense_pages

    spec = [{"rects": [_rect(100, 80)] * 2, "lines": [{}] * 5, "curves": []}]
    result = _with_fake_plumber(spec, lambda: graphic_dense_pages("any.pdf"))
    assert result == []


def test_graphic_dense_pages_ignores_tiny_rects():
    """Rects below min area (hairlines/borders) don't count toward the rect threshold."""
    from doc2md.figures import graphic_dense_pages

    # 10 tiny rects (5×5 = 25 pts² < 400) + 20 lines; big_rects=0 → not flagged
    spec = [{"rects": [_rect(5, 5)] * 10, "lines": [{}] * 20, "curves": []}]
    result = _with_fake_plumber(spec, lambda: graphic_dense_pages("any.pdf"))
    assert result == []


def test_graphic_dense_pages_returns_empty_without_pdfplumber():
    """If pdfplumber is not installed, graphic_dense_pages returns [] silently."""
    import sys
    from doc2md.figures import graphic_dense_pages

    orig = sys.modules.get("pdfplumber")
    sys.modules.pop("pdfplumber", None)
    try:
        result = graphic_dense_pages("any.pdf")
        assert result == []
    finally:
        if orig is not None:
            sys.modules["pdfplumber"] = orig


def test_graphic_dense_pages_multi_page_selective():
    """Only pages meeting both thresholds are returned; text-only pages are skipped."""
    from doc2md.figures import graphic_dense_pages

    spec = [
        {"rects": [_rect(100, 80)] * 6, "lines": [{}] * 12, "curves": []},  # p1: diagram
        {"rects": [], "lines": [], "curves": []},                              # p2: text-only
        {"rects": [_rect(100, 80)] * 8, "lines": [{}] * 10, "curves": [{}] * 3},  # p3: diagram
    ]
    result = _with_fake_plumber(spec, lambda: graphic_dense_pages("any.pdf"))
    assert result == [1, 3]


def test_engine_graphic_dense_creates_vision_work_items(tmp_path):
    """Engine must create infographic work items for graphic-dense pages when the
    primary parser sets no vision_pages and pdfplumber detects figure-heavy pages."""
    import sys, types
    from unittest.mock import patch, MagicMock
    from doc2md.engine import Engine
    from doc2md.parsers.base import ExtractionResult
    from doc2md.parsers.registry import ExtractorRegistry

    raw = tmp_path / "raw"
    raw.mkdir()
    # Must be .pdf so the graphic-dense fallback fires
    pdf_file = raw / "workflow.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 fake")

    class _FakePDFParser:
        name = "fakepdf"
        kinds = ("file",)
        extensions = (".pdf",)

        @property
        def available(self):
            return True

        def supports(self, source):
            return Path(source).suffix.lower() == ".pdf"

        def extract(self, source, *, ocr=False):
            # Returns text with no vision_pages — simulates pdf-inspector behaviour
            return ExtractionResult(
                text="BAGERA Global View workflow component node",
                parser=self.name,
            )

    reg = ExtractorRegistry([_FakePDFParser()], chains={".pdf": ["fakepdf"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", registry=reg, ocr=False)

    # Patch graphic_dense_pages in engine's namespace to return page 1
    # and patch _render_vision_pages to avoid needing pdf2image
    with patch("doc2md.engine.graphic_dense_pages", return_value=[1]):
        with patch.object(eng, "_render_vision_pages", return_value=[str(tmp_path / "p001.png")]):
            (tmp_path / "p001.png").write_bytes(b"fakepng")
            report = eng.convert_one(pdf_file)

    assert report.needs_llm, "Engine should have created a vision work item"
    kinds = [i["kind"] for i in report.items]
    assert "infographic" in kinds, f"Expected infographic work item, got: {kinds}"


# -- P1: graphic_dense_pages cached in manifest -------------------------

def test_page_analysis_cached_avoids_rerun(tmp_path):
    """graphic_dense_pages must not be called twice for a needs_llm file on rerun."""
    from unittest.mock import patch
    from doc2md.engine import Engine
    from doc2md.parsers.base import ExtractionResult
    from doc2md.parsers.registry import ExtractorRegistry

    raw = tmp_path / "raw"
    raw.mkdir()
    pdf_file = raw / "workflow.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 fake")

    class _FakePDF:
        name = "fakepdf"
        kinds = ("file",)
        extensions = (".pdf",)

        @property
        def available(self):
            return True

        def supports(self, source):
            return Path(source).suffix.lower() == ".pdf"

        def extract(self, source, *, ocr=False):
            return ExtractionResult(text="workflow diagram node", parser=self.name)

    reg = ExtractorRegistry([_FakePDF()], chains={".pdf": ["fakepdf"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", registry=reg, ocr=False)

    call_count = {"n": 0}
    original_dense = __import__("doc2md.figures", fromlist=["graphic_dense_pages"]).graphic_dense_pages

    def counting_dense(source, **kw):
        call_count["n"] += 1
        return [1]

    with patch("doc2md.engine.graphic_dense_pages", side_effect=counting_dense):
        with patch.object(eng, "_render_vision_pages", return_value=[str(tmp_path / "p.png")]):
            (tmp_path / "p.png").write_bytes(b"fake")
            r1 = eng.convert_one(pdf_file)
            assert r1.needs_llm
            assert call_count["n"] == 1, "first run should call graphic_dense_pages"

            # Second run: needs_llm is still True, but page_analysis is now cached
            r2 = eng.convert_one(pdf_file)
            assert call_count["n"] == 1, "second run must NOT call graphic_dense_pages again"


# -- P2: hash computed once per file ------------------------------------

def test_convert_one_accepts_precomputed_hash(tmp_path):
    """convert_one with a precomputed file_hash must not re-read the file."""
    from doc2md.engine import Engine
    from doc2md.manifest import hash_file
    from doc2md.parsers.base import ExtractionResult
    from doc2md.parsers.registry import ExtractorRegistry
    from unittest.mock import patch

    raw = tmp_path / "raw"
    raw.mkdir()
    f = raw / "a.md"
    f.write_text("hello world")

    class _P:
        name = "fake"
        kinds = ("file",)
        extensions = (".md",)

        @property
        def available(self):
            return True

        def supports(self, s):
            return Path(s).suffix.lower() == ".md"

        def extract(self, s, *, ocr=False):
            return ExtractionResult(text="hello world", parser=self.name)

    reg = ExtractorRegistry([_P()], chains={".md": ["fake"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", registry=reg, ocr=False)

    precomputed = hash_file(f)
    hash_calls = {"n": 0}
    original_hash = hash_file.__wrapped__ if hasattr(hash_file, "__wrapped__") else None

    with patch("doc2md.engine.hash_file", wraps=lambda p, **kw: (__import__("doc2md.manifest", fromlist=["hash_file"]).hash_file(p, **kw))) as mock_hash:
        eng.convert_one(f, file_hash=precomputed)
        # hash_file must not be called inside convert_one when precomputed hash supplied
        assert mock_hash.call_count == 0, "hash_file called despite precomputed hash"


# -- P3: mtime+size fast-path ------------------------------------------

def test_mtime_fastpath_skips_hash_read(tmp_path):
    """has_unchanged returns True via mtime+size without reading file bytes."""
    from doc2md.manifest import Manifest, FileRecord, hash_file
    from unittest.mock import patch

    cache = tmp_path / "cache"
    m = Manifest(cache)
    f = tmp_path / "doc.pdf"
    f.write_bytes(b"content")

    fh = hash_file(f)
    st = f.stat()
    m.upsert(FileRecord(
        original=str(f.resolve()), hash=fh, parser="fake",
        source=str(f), mtime=st.st_mtime, size=st.st_size,
    ))
    m.save()

    hash_calls = {"n": 0}
    original = hash_file

    def counting_hash(path, **kw):
        hash_calls["n"] += 1
        return original(path, **kw)

    with patch("doc2md.manifest.hash_file", side_effect=counting_hash):
        unchanged, rec = m.has_unchanged(str(f))

    assert unchanged is True
    assert hash_calls["n"] == 0, "hash_file must not be called when mtime+size match"


def test_mtime_changed_falls_back_to_hash(tmp_path):
    """If mtime differs, has_unchanged falls back to full hash comparison."""
    from doc2md.manifest import Manifest, FileRecord, hash_file
    import time

    cache = tmp_path / "cache"
    m = Manifest(cache)
    f = tmp_path / "doc.pdf"
    f.write_bytes(b"content")

    fh = hash_file(f)
    # Record a stale mtime (file appears modified)
    m.upsert(FileRecord(
        original=str(f.resolve()), hash=fh, parser="fake",
        source=str(f), mtime=0.0, size=f.stat().st_size,
    ))
    m.save()

    # Reload so we test a fresh instance
    m2 = Manifest(cache)
    unchanged, _ = m2.has_unchanged(str(f))
    # Hash is same, so should still be unchanged even though mtime was 0
    assert unchanged is True


# -- P4: batch save once ------------------------------------------------

def test_convert_all_saves_manifest_once(tmp_path):
    """convert_all must call manifest.save() once, not once per file."""
    from unittest.mock import patch
    from doc2md.engine import Engine
    from doc2md.parsers.base import ExtractionResult
    from doc2md.parsers.registry import ExtractorRegistry

    raw = tmp_path / "raw"
    raw.mkdir()
    for i in range(3):
        (raw / f"file{i}.md").write_text(f"content {i}")

    class _P:
        name = "fake"
        kinds = ("file",)
        extensions = (".md",)

        @property
        def available(self):
            return True

        def supports(self, s):
            return Path(s).suffix.lower() == ".md"

        def extract(self, s, *, ocr=False):
            return ExtractionResult(text=open(s).read(), parser=self.name)

    reg = ExtractorRegistry([_P()], chains={".md": ["fake"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", registry=reg, ocr=False)

    save_calls = {"n": 0}
    original_save = eng.manifest.save

    def counting_save():
        save_calls["n"] += 1
        original_save()

    eng.manifest.save = counting_save
    eng.convert_all(workers=1)

    assert save_calls["n"] == 1, f"Expected 1 save, got {save_calls['n']}"


# -- P5: zip not re-extracted when unchanged ----------------------------

def test_zip_not_re_extracted_when_unchanged(tmp_path):
    """_expand_zip must not call extractall a second time for an unchanged zip."""
    import zipfile as zf_mod
    from unittest.mock import patch, MagicMock
    from doc2md.engine import Engine

    raw = tmp_path / "raw"
    raw.mkdir()

    # Create a real zip with one txt file
    zip_path = raw / "docs.zip"
    with zf_mod.ZipFile(zip_path, "w") as zf:
        zf.writestr("a.txt", "hello")

    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", ocr=False)

    extract_calls = {"n": 0}
    original_extractall = zf_mod.ZipFile.extractall

    def counting_extractall(self, *args, **kwargs):
        extract_calls["n"] += 1
        return original_extractall(self, *args, **kwargs)

    with patch.object(zf_mod.ZipFile, "extractall", counting_extractall):
        eng._expand_zip(zip_path)  # first call — should extract
        eng._expand_zip(zip_path)  # second call — zip unchanged, must skip

    assert extract_calls["n"] == 1, f"extractall called {extract_calls['n']} times; expected 1"


# -- P6: parallel convert_all ------------------------------------------

def test_convert_all_parallel_returns_all_results(tmp_path):
    """convert_all with workers>1 must return one result per input file, in order."""
    from doc2md.engine import Engine
    from doc2md.parsers.base import ExtractionResult
    from doc2md.parsers.registry import ExtractorRegistry

    raw = tmp_path / "raw"
    raw.mkdir()
    names = [f"doc{i}.md" for i in range(5)]
    for name in names:
        (raw / name).write_text(f"content of {name}")

    class _P:
        name = "fake"
        kinds = ("file",)
        extensions = (".md",)

        @property
        def available(self):
            return True

        def supports(self, s):
            return Path(s).suffix.lower() == ".md"

        def extract(self, s, *, ocr=False):
            return ExtractionResult(text=open(s).read(), parser=self.name)

    reg = ExtractorRegistry([_P()], chains={".md": ["fake"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", registry=reg, ocr=False)
    results = eng.convert_all(workers=4)

    assert len(results) == 5
    sources = {Path(r.source).name for r in results if r.source}
    assert len(sources) == 5  # all distinct, no collisions


# -- P7: vision_dpi passed to render ------------------------------------

def test_engine_vision_dpi_passed_to_render(tmp_path):
    """Engine must pass vision_dpi to render_pdf_pages, not a hardcoded value."""
    from unittest.mock import patch
    from doc2md.engine import Engine
    from doc2md.parsers.base import ExtractionResult
    from doc2md.parsers.registry import ExtractorRegistry

    raw = tmp_path / "raw"
    raw.mkdir()
    pdf_file = raw / "chart.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 fake")

    class _FakePDF:
        name = "fakepdf"
        kinds = ("file",)
        extensions = (".pdf",)

        @property
        def available(self):
            return True

        def supports(self, s):
            return Path(s).suffix.lower() == ".pdf"

        def extract(self, s, *, ocr=False):
            return ExtractionResult(text="diagram node", parser=self.name)

    reg = ExtractorRegistry([_FakePDF()], chains={".pdf": ["fakepdf"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache",
                 registry=reg, ocr=False, vision_dpi=72)

    render_calls = []

    def fake_render(path, *, first, last, dpi):
        render_calls.append(dpi)
        return []  # no images — keeps test simple

    with patch("doc2md.engine.graphic_dense_pages", return_value=[1]):
        with patch("doc2md.engine.render_pdf_pages", side_effect=fake_render):
            eng.convert_one(pdf_file)

    assert render_calls, "render_pdf_pages was never called"
    assert all(d == 72 for d in render_calls), f"Expected dpi=72, got {render_calls}"


def test_engine_vision_dpi_default_is_150(tmp_path):
    """Default vision_dpi must be 150, not the old 200/300."""
    from doc2md.engine import Engine

    eng = Engine(tmp_path / "raw", tmp_path / "sources", tmp_path / "cache", ocr=False)
    assert eng.vision_dpi == 150


# -- image_dominant_pages: raster-PDF fallback detection -----------------


def _fake_plumber_with_images(pages_spec: list[dict]):
    """Build a fake pdfplumber module for image_dominant_pages testing.

    Each spec: width (float), height (float), images (list of dicts with
    x0, x1, top, bottom keys matching pdfplumber's coordinate system).
    """
    import sys
    import types

    fake = types.ModuleType("pdfplumber")

    class _FakePage:
        def __init__(self, spec):
            self.width = spec.get("width", 100.0)
            self.height = spec.get("height", 100.0)
            self.images = spec.get("images", [])

    class _FakePDF:
        def __init__(self, specs):
            self.pages = [_FakePage(s) for s in specs]

        def __enter__(self):
            return self

        def __exit__(self, *a):
            pass

    fake.open = lambda source: _FakePDF(pages_spec)
    return fake


def _with_fake_plumber_images(pages_spec, fn):
    import sys

    fake = _fake_plumber_with_images(pages_spec)
    orig = sys.modules.get("pdfplumber")
    sys.modules["pdfplumber"] = fake
    try:
        return fn()
    finally:
        if orig is not None:
            sys.modules["pdfplumber"] = orig
        else:
            sys.modules.pop("pdfplumber", None)


def test_image_dominant_pages_flags_raster_page():
    """A page whose embedded image covers 90% of the area is flagged for vision."""
    from doc2md.figures import image_dominant_pages

    # 100×100 pt page; one 95×95 image = 90.25% coverage → above 40% threshold
    spec = [{"width": 100.0, "height": 100.0,
             "images": [{"x0": 0, "x1": 95, "top": 0, "bottom": 95}]}]
    result = _with_fake_plumber_images(spec, lambda: image_dominant_pages("any.pdf"))
    assert result == [1]


def test_image_dominant_pages_ignores_small_images():
    """A decorative image covering only 9% of the page does not trigger vision."""
    from doc2md.figures import image_dominant_pages

    # 100×100 pt page; one 30×30 image = 9% coverage → below 40% threshold
    spec = [{"width": 100.0, "height": 100.0,
             "images": [{"x0": 0, "x1": 30, "top": 0, "bottom": 30}]}]
    result = _with_fake_plumber_images(spec, lambda: image_dominant_pages("any.pdf"))
    assert result == []


def test_image_dominant_pages_multi_page_selective():
    """Only raster-heavy pages are returned; text-only pages are skipped."""
    from doc2md.figures import image_dominant_pages

    spec = [
        # p1: full-page slide screenshot (100% coverage)
        {"width": 100.0, "height": 100.0,
         "images": [{"x0": 0, "x1": 100, "top": 0, "bottom": 100}]},
        # p2: no images at all
        {"width": 100.0, "height": 100.0, "images": []},
        # p3: half-page chart (50% coverage)
        {"width": 100.0, "height": 100.0,
         "images": [{"x0": 0, "x1": 100, "top": 0, "bottom": 50}]},
    ]
    result = _with_fake_plumber_images(spec, lambda: image_dominant_pages("any.pdf"))
    assert result == [1, 3]


def test_image_dominant_pages_returns_empty_without_pdfplumber():
    """If pdfplumber is unavailable, image_dominant_pages returns [] silently."""
    import sys
    from doc2md.figures import image_dominant_pages

    orig = sys.modules.get("pdfplumber")
    sys.modules.pop("pdfplumber", None)
    try:
        result = image_dominant_pages("any.pdf")
        assert result == []
    finally:
        if orig is not None:
            sys.modules["pdfplumber"] = orig


def test_save_vision_image_resizes_oversized(tmp_path):
    """_save_vision_image must downscale images that exceed max_image_dim."""
    Image = pytest.importorskip("PIL.Image")
    from doc2md.engine import Engine

    eng = Engine(tmp_path / "raw", tmp_path / "sources", tmp_path / "cache",
                 ocr=False, max_image_dim=200)
    big = Image.new("RGB", (600, 400), color=(128, 128, 128))
    dest = tmp_path / "out.jpg"
    eng._save_vision_image(big, dest)

    result = Image.open(dest)
    assert max(result.width, result.height) <= 200, (
        f"Expected ≤200px, got {result.width}x{result.height}"
    )
    assert abs(result.width / result.height - 600 / 400) < 0.05


def test_save_vision_image_leaves_small_image_unchanged(tmp_path):
    """_save_vision_image must not upscale images that are already within the cap."""
    Image = pytest.importorskip("PIL.Image")
    from doc2md.engine import Engine

    eng = Engine(tmp_path / "raw", tmp_path / "sources", tmp_path / "cache",
                 ocr=False, max_image_dim=1568)
    small = Image.new("RGB", (800, 600), color=(0, 0, 255))
    dest = tmp_path / "out.jpg"
    eng._save_vision_image(small, dest)

    result = Image.open(dest)
    assert result.size == (800, 600), f"Size changed unexpectedly: {result.size}"


def test_render_vision_pages_heals_oversized_cache(tmp_path):
    """Cached images that exceed max_image_dim are re-rendered, not reused."""
    Image = pytest.importorskip("PIL.Image")
    from unittest.mock import patch
    from doc2md.engine import Engine
    from doc2md.parsers.base import ExtractionResult
    from doc2md.parsers.registry import ExtractorRegistry

    raw = tmp_path / "raw"
    raw.mkdir()

    class _Dummy:
        name = "fake"
        kinds = ("file",)
        extensions = (".pdf",)

        @property
        def available(self):
            return True

        def supports(self, s):
            return True

        def extract(self, s, *, ocr=False):
            return ExtractionResult(text="x", parser=self.name)

    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache",
                 registry=ExtractorRegistry([_Dummy()], chains={}),
                 ocr=False, max_image_dim=200)

    img_dir = tmp_path / "cache" / "images" / "testhash"
    img_dir.mkdir(parents=True)
    img_path = img_dir / "page-001.jpg"
    Image.new("RGB", (800, 600)).save(img_path, "JPEG")

    replacement = Image.new("RGB", (400, 300), color=(255, 0, 0))
    render_calls = []

    def fake_render(path, *, first, last, dpi):
        render_calls.append(first)
        return [replacement]

    with patch("doc2md.engine.render_pdf_pages", side_effect=fake_render):
        result = eng._render_vision_pages(
            Path(raw / "x.pdf"), "testhash", [1]
        )

    assert render_calls == [1], "Should have re-rendered the oversized cached image"
    assert result
    final = Image.open(result[0])
    assert max(final.width, final.height) <= 200, f"Still oversized: {final.size}"


def test_engine_uses_image_dominant_when_no_vector_graphics(tmp_path):
    """When graphic_dense_pages returns [], image_dominant_pages fires as fallback.

    This is the WhatsApp screenshot PDF scenario: the PDF contains raster slides
    with zero vector elements, so the vector heuristic misses them entirely.
    """
    from unittest.mock import patch
    from doc2md.engine import Engine
    from doc2md.parsers.base import ExtractionResult
    from doc2md.parsers.registry import ExtractorRegistry

    raw = tmp_path / "raw"
    raw.mkdir()
    pdf_file = raw / "screenshot.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 fake")

    class _FakePDFParser:
        name = "fakepdf"
        kinds = ("file",)
        extensions = (".pdf",)

        @property
        def available(self):
            return True

        def supports(self, source):
            return Path(source).suffix.lower() == ".pdf"

        def extract(self, source, *, ocr=False):
            # Partial text layer extracted from image-PDF — looks valid but incomplete
            return ExtractionResult(
                text="Airport passenger processing timeline architecture overview",
                parser=self.name,
            )

    reg = ExtractorRegistry([_FakePDFParser()], chains={".pdf": ["fakepdf"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", registry=reg, ocr=False)

    with patch("doc2md.engine.graphic_dense_pages", return_value=[]):
        with patch("doc2md.engine.image_dominant_pages", return_value=[1]) as mock_idp:
            with patch.object(eng, "_render_vision_pages",
                              return_value=[str(tmp_path / "p.png")]):
                (tmp_path / "p.png").write_bytes(b"fakepng")
                report = eng.convert_one(pdf_file)

    mock_idp.assert_called_once()
    assert report.needs_llm, "Should have created a vision work item for the raster page"
    kinds = [i["kind"] for i in report.items]
    assert "infographic" in kinds, f"Expected infographic item, got: {kinds}"


def test_engine_image_dominant_not_called_when_vector_present(tmp_path):
    """When graphic_dense_pages already returns pages, image_dominant_pages is skipped."""
    from unittest.mock import patch
    from doc2md.engine import Engine
    from doc2md.parsers.base import ExtractionResult
    from doc2md.parsers.registry import ExtractorRegistry

    raw = tmp_path / "raw"
    raw.mkdir()
    pdf_file = raw / "workflow.pdf"
    pdf_file.write_bytes(b"%PDF-1.4 fake")

    class _FakePDFParser:
        name = "fakepdf"
        kinds = ("file",)
        extensions = (".pdf",)

        @property
        def available(self):
            return True

        def supports(self, source):
            return Path(source).suffix.lower() == ".pdf"

        def extract(self, source, *, ocr=False):
            return ExtractionResult(text="workflow node diagram", parser=self.name)

    reg = ExtractorRegistry([_FakePDFParser()], chains={".pdf": ["fakepdf"]})
    eng = Engine(raw, tmp_path / "sources", tmp_path / "cache", registry=reg, ocr=False)

    with patch("doc2md.engine.graphic_dense_pages", return_value=[1]):
        with patch("doc2md.engine.image_dominant_pages") as mock_idp:
            with patch.object(eng, "_render_vision_pages",
                              return_value=[str(tmp_path / "p.png")]):
                (tmp_path / "p.png").write_bytes(b"fakepng")
                eng.convert_one(pdf_file)

    mock_idp.assert_not_called()