"""Manifest + content-addressed caches.

The manifest is the source of truth: ``original → hash → parser → source``.
Caches are keyed by content hash so unchanged files skip re-work and re-runs
spend zero LLM tokens. ``hash-delta`` re-runs are detected by comparing the
file's current hash to the manifest entry.
"""

from __future__ import annotations

import hashlib
import json
import threading
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


def hash_file(path: str | Path, *, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


@dataclass
class FileRecord:
    original: str
    hash: str
    parser: str
    source: Optional[str] = None
    complexity: str = "none"
    images: list[str] = field(default_factory=list)
    work_order: Optional[str] = None  # path to the skill work-order JSON, if any
    needs_llm: bool = False
    failed: bool = False  # extraction yielded no text; skip re-runs without a source
    # Token tracking for cost/traceability
    tokens_raw: int = 0          # Before optimization
    tokens_optimised: int = 0    # After optimization (input to LLM)
    tokens_llm_input: int = 0    # Sent to Claude (work items)
    tokens_llm_output: int = 0   # Received from Claude
    # P3: stat fast-path — avoids full hash read when mtime+size unchanged
    mtime: float = 0.0
    size: int = 0

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "FileRecord":
        return cls(**{k: d.get(k) for k in (
            "original", "hash", "parser", "source", "complexity",
            "images", "work_order", "needs_llm", "failed",
            "tokens_raw", "tokens_optimised", "tokens_llm_input", "tokens_llm_output",
            "mtime", "size",
        )})


class Manifest:
    def __init__(self, cache_dir: str | Path) -> None:
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.path = self.cache_dir / "manifest.json"
        self._files: dict[str, FileRecord] = {}
        self._lock = threading.Lock()
        self._load()

    def _load(self) -> None:
        if self.path.exists():
            try:
                data = json.loads(self.path.read_text())
            except Exception:
                data = {}
            for k, v in data.get("files", {}).items():
                self._files[k] = FileRecord.from_dict(v)

    def save(self) -> None:
        with self._lock:
            snapshot = {k: v.to_dict() for k, v in self._files.items()}
        self.path.write_text(
            json.dumps({"files": snapshot}, indent=2, sort_keys=True)
        )

    # -- lookup --------------------------------------------------------

    def get(self, original: str) -> Optional[FileRecord]:
        return self._files.get(str(Path(original).resolve()))

    @staticmethod
    def _usable(rec: Optional[FileRecord]) -> bool:
        # A failed record with no source must be re-tried after the failure
        # cause is fixed; only cached successes with an existing source are
        # considered up-to-date.
        return rec is not None and not rec.failed and bool(rec.source and Path(rec.source).exists())

    def is_current(self, original: str, file_hash: str) -> tuple[bool, Optional[FileRecord]]:
        """Like has_unchanged but with a precomputed hash (no re-read)."""
        rec = self.get(original)
        if not self._usable(rec):
            return False, rec
        return (file_hash == rec.hash, rec)

    def has_unchanged(self, original: str) -> tuple[bool, Optional[FileRecord]]:
        rec = self.get(original)
        if not self._usable(rec):
            return False, rec
        # P3: mtime+size fast-path — skip the full hash read when stat matches
        try:
            st = Path(original).stat()
            if rec.mtime and rec.mtime == st.st_mtime and rec.size == st.st_size:
                return True, rec
            current = hash_file(original)
        except OSError:
            return False, rec
        return (current == rec.hash, rec)

    def upsert(self, record: FileRecord) -> None:
        with self._lock:
            self._files[str(Path(record.original).resolve())] = record

    def mark_done(self, source_path: str | Path) -> Optional[FileRecord]:
        """Clear needs_llm on the record whose source matches (path-resolved both sides)."""
        target = str(Path(source_path).resolve())
        for rec in self._files.values():
            if rec.source and str(Path(rec.source).resolve()) == target:
                rec.needs_llm = False
                self.save()
                return rec
        return None

    # -- content-addressed caches --------------------------------------
    # Extraction cache stores the full result (text + images + meta) as JSON so
    # re-runs of pending-LLM files reuse it without re-running parsers or losing
    # infographic/vision signals.

    def extraction_cache_path(self, file_hash: str, parser: str) -> Path:
        return self.cache_dir / "extractions" / f"{file_hash}.{parser}.json"

    def mermaid_cache_path(self, file_hash: str, key: str) -> Path:
        safe = key.replace("/", "_")
        return self.cache_dir / "mermaid" / f"{file_hash}.{safe}.mmd"

    def work_cache_path(self, file_hash: str, item_id: str) -> Path:
        safe = item_id.replace("/", "_")
        return self.cache_dir / "work" / f"{file_hash}.{safe}.md"

    def page_analysis_cache_path(self, file_hash: str) -> Path:
        # v2: added raster-image (image_dominant_pages) detection alongside vector heuristic.
        # Old .json entries are silently ignored — returns None → triggers fresh analysis.
        return self.cache_dir / "page_analysis" / f"{file_hash}.v2.json"

    def get_extraction(self, file_hash: str, parser: str) -> Optional[dict]:
        p = self.extraction_cache_path(file_hash, parser)
        if not p.exists():
            return None
        try:
            return json.loads(p.read_text())
        except Exception:
            return None

    def set_extraction(self, file_hash: str, parser: str, obj: dict) -> Path:
        p = self.extraction_cache_path(file_hash, parser)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj))
        return p

    def get_mermaid(self, file_hash: str, key: str) -> Optional[str]:
        p = self.mermaid_cache_path(file_hash, key)
        return p.read_text() if p.exists() else None

    def set_mermaid(self, file_hash: str, key: str, text: str) -> Path:
        p = self.mermaid_cache_path(file_hash, key)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p

    def get_work(self, file_hash: str, item_id: str) -> Optional[str]:
        p = self.work_cache_path(file_hash, item_id)
        return p.read_text() if p.exists() else None

    def set_work(self, file_hash: str, item_id: str, content: str) -> Path:
        p = self.work_cache_path(file_hash, item_id)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
        return p

    # P1: graphic_dense_pages result — deterministic on file content, cached by hash
    def get_page_analysis(self, file_hash: str) -> Optional[list[int]]:
        p = self.page_analysis_cache_path(file_hash)
        if not p.exists():
            return None
        try:
            return json.loads(p.read_text())
        except Exception:
            return None

    def set_page_analysis(self, file_hash: str, pages: list[int]) -> Path:
        p = self.page_analysis_cache_path(file_hash)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(pages))
        return p

    # -- bulk ----------------------------------------------------------

    def sources(self) -> list[str]:
        return [r.source for r in self._files.values() if r.source]
