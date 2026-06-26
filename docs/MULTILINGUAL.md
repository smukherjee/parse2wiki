# Multilingual Document Support

doc2md now supports automatic language detection and multilingual OCR for documents containing non-Latin scripts.

## Supported Scripts

| Script | Languages | Unicode Range |
|--------|-----------|---------------|
| Arabic | Arabic, Persian, Urdu | U+0600–U+06FF |
| Devanagari | Hindi, Sanskrit, Marathi | U+0900–U+097F |
| Bengali | Bengali, Assamese | U+0980–U+09FF |
| CJK | Chinese, Japanese | U+4E00–U+9FFF |
| Hangul | Korean | U+AC00–U+D7AF |
| Hiragana/Katakana | Japanese | U+3040–U+30FF |
| Cyrillic | Russian, Ukrainian, Bulgarian | U+0400–U+04FF |
| Greek | Greek | U+0370–U+03FF |
| Hebrew | Hebrew, Yiddish | U+0590–U+05FF |
| Thai | Thai, Lao | U+0E00–U+0E7F |

## Quick Start

### 1. Install Tesseract Language Packs

**macOS (Homebrew):**
```bash
brew install tesseract-lang
```

**Ubuntu/Debian:**
```bash
# Arabic
sudo apt install tesseract-ocr-ara

# Hindi
sudo apt install tesseract-ocr-hin

# All languages
sudo apt install tesseract-ocr-all
```

### 2. Verify Installation

```bash
# Check installed languages
doc2md tesseract-langs

# Test language detection
doc2md detect-lang --text "Your text sample here"
```

### 3. Convert Multilingual Documents

```bash
# Standard conversion (automatically detects languages)
doc2md convert --ocr

# Force multilingual parser for PDFs
doc2md convert --parser pdf-multilingual
```

## How It Works

### Language Detection

1. **Script Detection**: Analyzes Unicode character ranges to identify scripts present in the text
2. **Language Identification**: Uses `langdetect` library for confident language detection
3. **Tesseract Routing**: Automatically selects appropriate language packs for OCR

### OCR Pipeline

```
Document → Text Extraction (pymupdf4llm)
              ↓
         Valid Text?
         /         \
       Yes          No
        ↓            ↓
   Check Script   OCR with
   for non-Latin  detected langs
        ↓            ↓
   Add lang     Return OCR
   metadata     text + langs
```

## API Usage

### Detect Language

```python
from doc2md.lang import detect_language, detect_script, get_tesseract_langs_for_text

text = "EGYPTIAN AIRPORTS COMPANY\nالشركة المصرية للمطارات"

# Detect primary language
result = detect_language(text)
print(f"Language: {result.language}")  # 'ar'
print(f"Script: {result.script}")      # 'arabic'

# Get required Tesseract languages
langs = get_tesseract_langs_for_text(text)
print(langs)  # ['eng', 'ara']

# Detailed script analysis
scripts = detect_script(text)
for s in scripts:
    print(f"{s.script}: {s.char_count} chars")
```

### Multilingual OCR

```python
from doc2md.ocr import ocr_image_multilingual, ocr_pdf_multilingual

# Image OCR
text, langs = ocr_image_multilingual("path/to/image.png")
print(f"OCR text in languages: {langs}")

# PDF OCR
results = ocr_pdf_multilingual("path/to/document.pdf")
for page_num, text, langs in results:
    print(f"Page {page_num}: {langs}")
```

## CLI Commands

### `doc2md tesseract-langs`

Shows installed Tesseract language packs and installation commands for missing ones.

### `doc2md detect-lang`

Analyzes text sample for language/script detection.

```bash
# From command line
doc2md detect-lang --text "Sample text" --show-scripts

# From file
doc2md detect-lang --file document.txt
```

## Parser Comparison

For accuracy testing, compare parsers on multilingual documents:

```bash
# Run all parsers and compare output
doc2md convert --compare

# Compare specific parsers
doc2md convert --parser pymupdf4llm
doc2md convert --parser pdf-multilingual
```

## Metadata

Extracted language information is stored in the manifest:

```json
{
  "detected_language": "ar",
  "detected_script": "arabic",
  "ocr_languages": ["eng", "ara"],
  "ocr_pages": 12
}
```

## Troubleshooting

### "tesseract not available"

Install Tesseract OCR:
```bash
# macOS
brew install tesseract tesseract-lang

# Ubuntu/Debian
sudo apt install tesseract-ocr tesseract-ocr-eng tesseract-ocr-ara
```

### "Language pack not installed"

The detected language requires a specific Tesseract data file:
```bash
# Check what's installed
tesseract --list-langs

# Install missing language
brew install tesseract-lang  # macOS
sudo apt install tesseract-ocr-ara  # Ubuntu
```

### Poor OCR Quality

1. Increase DPI: `--dpi 300` (default: 200)
2. Ensure correct language packs are installed
3. Try forcing the multilingual parser: `--parser pdf-multilingual`

## Example: Arabic/English RFP

```bash
# Convert Egyptian RFP with Arabic/English content
doc2md convert --ocr

# Output shows detected languages
# llm  pymupdf4llm  raw/RFP.pdf → sources/RFP.pdf.md
#       ! Non-Latin script detected: arabic
#       ! OCR languages: eng+ara
```

## Files Added

| File | Purpose |
|------|---------|
| `doc2md/lang.py` | Language/script detection |
| `doc2md/ocr.py` | Multilingual OCR functions |
| `doc2md/parsers/pdf_multilingual.py` | PDF parser with language detection |
| `doc2md/parsers/image.py` | Updated image parser with multilingual OCR |
| `doc2md/cli.py` | Added `tesseract-langs` and `detect-lang` commands |
