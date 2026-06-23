#!/usr/bin/env python3
"""
Wiki ingestion: write source summaries and update index/log.
"""

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class WikiConfig:
    """Configuration for wiki ingestion."""
    base_path: str
    wiki_path: str = "wiki"
    index_file: str = "index.md"
    log_file: str = "log.md"
    sources_dir: str = "wiki/sources"
    require_review: bool = True


class WikiIngester:
    """Handles wiki source page creation and index updates."""

    def __init__(self, config: WikiConfig):
        self.config = config
        self.base = Path(config.base_path)
        self.wiki = self.base / config.wiki_path
        self.sources_dir = self.wiki / config.sources_dir

    def ensure_directories(self):
        """Create wiki directories if they don't exist."""
        self.sources_dir.mkdir(parents=True, exist_ok=True)

    def generate_source_filename(self, source_path: str) -> str:
        """
        Generate a kebab-case filename from source path.

        Examples:
            GLOBAL VIEW-WORKFLOW-VISTA.pdf → global-view-vista.md
            INFOPAX_DESC_US.pdf → infopax-desc.md
        """
        name = Path(source_path).stem
        name = name.replace('_US', '').replace('_UK', '')
        name = name.replace('_DESC', '-desc')
        name = name.replace('_OVERVIEW', '-overview')
        name = name.replace('_', '-').replace(' ', '-').lower()
        name = re.sub(r'-+', '-', name)  # Collapse multiple dashes
        name = name.strip('-')
        return f"{name}.md"

    def write_source_page(
        self,
        content: str,
        source_path: str,
        filename: Optional[str] = None
    ) -> Path:
        """
        Write a source summary page.

        Args:
            content: Complete markdown with frontmatter
            source_path: Original source file path
            filename: Optional custom filename

        Returns:
            Path to written file
        """
        if filename is None:
            filename = self.generate_source_filename(source_path)

        output_path = self.sources_dir / filename
        output_path.write_text(content, encoding='utf-8')
        return output_path

    def update_index(
        self,
        source_filename: str,
        description: str,
        section: str = "Source Summaries"
    ):
        """
        Add entry to wiki/index.md.

        Args:
            source_filename: Name of new source file (without wiki/sources/)
            description: One-line description
            section: Section in index to update
        """
        index_path = self.wiki / self.config.index_file

        if not index_path.exists():
            self._create_index()

        content = index_path.read_text(encoding='utf-8')

        # Generate wikilink
        wikilink = f"[[{source_filename.replace('.md', '')}]]"

        # Check if already indexed
        if wikilink in content:
            return  # Already indexed

        # Find the section and add entry
        section_pattern = rf"(## {re.escape(section)}\n\n.*?)(\n\n##|\Z)"

        def add_entry(match):
            section_content = match.group(1)
            # Add new entry as table row or list item
            new_entry = f"\n| [[{source_filename.replace('.md', '')}]] | {description} |"
            return section_content.rstrip() + new_entry + "\n" + (match.group(2) or "")

        new_content = re.sub(section_pattern, add_entry, content, flags=re.DOTALL)

        # If section not found, append at end
        if new_content == content:
            new_content = content + f"\n\n## {section}\n\n| [[{source_filename.replace('.md', '')}]] | {description} |\n"

        index_path.write_text(new_content, encoding='utf-8')

    def update_log(self, operation: str, details: str):
        """
        Append entry to wiki/log.md.

        Args:
            operation: Operation type (Ingest, Correction, Lint, etc.)
            details: Operation details in markdown
        """
        log_path = self.wiki / self.config.log_file

        if not log_path.exists():
            log_path.write_text("# Wiki Operation Log\n\nAppend-only log of all wiki operations.\n\n---\n\n")

        today = date.today().isoformat()
        entry = f"## {today} — {operation}\n\n{details}\n\n---\n\n"

        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(entry)

    def _create_index(self):
        """Create a minimal index file if none exists."""
        index_content = """# Wiki — Master Index

Last updated: TBD

## About

Brief description of this wiki.

---

## Source Summaries

| Page | Source Document |
|------|----------------|

---

## Concepts

| Page | Description |
|------|-------------|

"""
        index_path = self.wiki / self.config.index_file
        index_path.write_text(index_content, encoding='utf-8')

    def check_existing(self, source_path: str) -> bool:
        """
        Check if a source has already been ingested.

        Args:
            source_path: Original source file path

        Returns:
            True if already ingested
        """
        filename = self.generate_source_filename(source_path)
        return (self.sources_dir / filename).exists()
