# parse2wiki

Convert PDF, DOCX, PPTX, XLSX, and ZIP files into wiki-ready markdown with automatic Mermaid diagram generation.

## Features

- **Zero-token extraction** — Uses `pdftotext`, `tesseract`, `pandoc` for initial extraction
- **Smart diagram detection** — Classifies diagrams as simple (deterministic Mermaid) vs complex (LLM-assisted)
- **Token-optimized** — Only invokes LLM for complex diagrams and final summarization
- **Wiki-agnostic** — Works with any wiki that uses markdown + frontmatter

## Installation

```bash
# Clone and install
git clone https://github.com/sujoymukherjee/parse2wiki.git
cd parse2wiki
pip install -e .

# Verify installation
parse2wiki-extract --version
parse2wiki-check --version
```

## Quick Start

### 1. Create a config file

```yaml
# .parse2wiki.yaml
project:
  name: "My Wiki"
  base_path: "/path/to/project"

sources:
  input_dir: "raw"
  skip_already_processed: true

wiki:
  path: "wiki"
  index_file: "index.md"
  log_file: "log.md"
  sources_dir: "wiki/sources"

llm:
  enabled: true
  model: "claude-sonnet-4-6"
  only_complex_diagrams: true
```

### 2. Check for new files

```bash
parse2wiki-check --config .parse2wiki.yaml
```

### 3. Extract text (zero tokens)

```bash
parse2wiki-extract --config .parse2wiki.yaml --input raw/ --output outputs/extractions/
```

### 4. Ingest into wiki (LLM-assisted summarization)

```bash
parse2wiki-ingest --config .parse2wiki.yaml --review-first
```

## CLI Commands

### `parse2wiki-check`

Check for new/unprocessed files in the source directory.

```bash
parse2wiki-check --config .parse2wiki.yaml --json  # Output as JSON
```

### `parse2wiki-extract`

Extract text from documents.

```bash
# Extract all files
parse2wiki-extract --input raw/ --output outputs/extractions/

# With OCR enabled
parse2wiki-extract --input raw/ --output outputs/extractions/ --ocr

# Dry run (show what would be processed)
parse2wiki-extract --input raw/ --dry-run
```

### `parse2wiki-ingest`

Generate wiki source summaries and update index.

```bash
# Interactive review mode
parse2wiki-ingest --config .parse2wiki.yaml --review-first

# Auto-approve (no review)
parse2wiki-ingest --config .parse2wiki.yaml --auto-approve
```

## Supported File Types

| Extension | Extraction Method | Mermaid Support |
|-----------|-------------------|-----------------|
| `.pdf` | pdftotext + tesseract OCR | Yes (workflow diagrams) |
| `.docx` | python-docx | Yes (embedded diagrams) |
| `.pptx` | python-pptx | Yes (slide flows) |
| `.xlsx` | openpyxl → markdown tables | No |
| `.zip` | unzip → recurse | Depends on contents |

## Diagram Detection

The tool automatically detects diagram/workflow content using keyword patterns:

- **Simple diagrams** → Deterministic Mermaid generation (0 tokens)
- **Complex diagrams** → Flagged for LLM processing (requires approval)

## Token Optimization

| Stage | Token Cost |
|-------|------------|
| Text extraction | 0 |
| OCR | 0 |
| Diagram detection | 0 |
| Simple Mermaid generation | 0 |
| Complex diagram interpretation | ~500-1500 per diagram |
| Wiki summary generation | ~500-1000 per document |

**Typical savings: 80-90% vs naive LLM extraction**

## License

MIT
