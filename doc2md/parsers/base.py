"""The Parser seam.

A Parser is a pluggable adapter that performs extraction (zero-token,
deterministic recovery of text + structure) for a set of source kinds or
file extensions. Adapters may wrap a Python library *or* an external binary
of any language (Rust/Go/CLI) — see :class:`SubprocessParser`.

Every extraction records which parser produced it, so accuracy can be
audited and ``--compare`` can diff parsers on the same file.
"""

from __future__ import annotations

import importlib
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol, runtime_checkable


@dataclass
class ExtractionResult:
    """Normalised output of one parser run on one document.

    ``text`` is markdown. ``images`` holds paths to extracted
    diagram/infographic images that the skill must send to Claude vision.
    """

    text: str
    parser: str
    used_fallback: bool = False
    warnings: list[str] = field(default_factory=list)
    images: list[str] = field(default_factory=list)
    meta: dict = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return bool(self.text and self.text.strip())


@runtime_checkable
class Parser(Protocol):
    """Structural contract every parser adapter satisfies."""

    name: str
    kinds: tuple[str, ...]

    def supports(self, source: str) -> bool: ...
    @property
    def available(self) -> bool: ...
    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult: ...


class SubprocessParser:
    """Base for parsers that wrap an external binary of any language.

    Subclasses set ``name``/``binary``/``extensions`` and implement
    :meth:`args` and (optionally) :meth:`parse`. Availability is resolved via
    ``shutil.which``, so a missing binary degrades to a fallback-chain entry
    rather than a crash.
    """

    name: str = ""
    binary: str = ""
    extensions: tuple[str, ...] = ()
    kinds: tuple[str, ...] = ("file",)
    timeout: int = 180

    def __init__(self) -> None:
        if not self.name:
            raise TypeError(f"{type(self).__name__} must set .name")

    @property
    def available(self) -> bool:
        return bool(self.binary) and shutil.which(self.binary) is not None

    def supports(self, source: str) -> bool:
        ext = Path(source).suffix.lower()
        return ext in self.extensions if self.extensions else True

    def args(self, source: str, *, ocr: bool) -> list[str]:
        raise NotImplementedError

    def parse(self, stdout: str, source: str) -> str:
        """Map raw stdout to markdown. Default: pass through."""
        return stdout

    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult:
        try:
            proc = subprocess.run(
                [self.binary, *self.args(source, ocr=ocr)],
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )
        except subprocess.TimeoutExpired:
            return ExtractionResult(
                text="", parser=self.name, warnings=[f"{self.name} timeout after {self.timeout}s"]
            )
        except FileNotFoundError:
            return ExtractionResult(text="", parser=self.name, warnings=[f"{self.name} not on PATH"])
        if proc.returncode != 0:
            err = (proc.stderr or "").strip().splitlines()
            msg = err[-1] if err else f"{self.name} exit {proc.returncode}"
            return ExtractionResult(text="", parser=self.name, warnings=[msg[:200]])
        text = self.parse(proc.stdout, source)
        return ExtractionResult(text=text, parser=self.name)


class LibraryParser:
    """Base for parsers that wrap a Python library imported lazily.

    Subclasses set ``name``/``module_name``/``extensions`` and implement
    :meth:`extract`. Availability is resolved by importing ``module_name``, so
    a missing optional dependency degrades to a fallback-chain entry rather
    than a crash. Eliminates the duplicated available/supports copy-paste.
    """

    name: str = ""
    module_name: str = ""
    extensions: tuple[str, ...] = ()
    kinds: tuple[str, ...] = ("file",)

    def __init__(self) -> None:
        if not self.name:
            raise TypeError(f"{type(self).__name__} must set .name")

    @property
    def available(self) -> bool:
        try:
            importlib.import_module(self.module_name)
        except Exception:
            return False
        return True

    def supports(self, source: str) -> bool:
        ext = Path(source).suffix.lower()
        return ext in self.extensions if self.extensions else True

    def extract(self, source: str, *, ocr: bool = False) -> ExtractionResult:
        raise NotImplementedError