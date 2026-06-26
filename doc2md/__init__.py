"""doc2md — a deterministic pre-processor that turns documents into
token-optimised markdown + Mermaid for an external LLM-wiki builder.

This package is the *deterministic engine*. It never calls an LLM. The only
LLM work in doc2md (complex text-diagram Mermaid + infographic interpretation
via Claude vision) lives in the ``/doc2md`` Claude skill, which calls the
engine as a library.
"""

from __future__ import annotations

from .engine import Engine
from .parsers import build_registry
from .parsers.base import ExtractionResult, Parser, SubprocessParser
from .parsers.registry import ExtractorRegistry

__all__ = [
    "Engine",
    "ExtractionResult",
    "Parser",
    "SubprocessParser",
    "ExtractorRegistry",
    "build_registry",
]

__version__ = "0.1.0"