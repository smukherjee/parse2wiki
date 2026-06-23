"""LLM-assisted summarization for wiki ingestion."""

from .wiki_summary import summarize_for_wiki, SummarizerConfig

__all__ = ["summarize_for_wiki", "SummarizerConfig"]
