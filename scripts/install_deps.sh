#!/usr/bin/env bash
# install_deps.sh — install all optional doc2md dependencies in one shot.
#
# Run from the repo root:
#   bash scripts/install_deps.sh [--mineru] [--no-brew] [--no-cargo]
#
# Flags:
#   --mineru      also install MinerU (magic-pdf[full]) — heavy, ~2 GB model download
#   --no-brew     skip Homebrew packages  (e.g. inside Docker/CI)
#   --no-cargo    skip Rust/Cargo packages

set -euo pipefail

INSTALL_MINERU=0
SKIP_BREW=0
SKIP_CARGO=0

for arg in "$@"; do
  case $arg in
    --mineru)    INSTALL_MINERU=1 ;;
    --no-brew)   SKIP_BREW=1 ;;
    --no-cargo)  SKIP_CARGO=1 ;;
    *) echo "Unknown flag: $arg"; exit 1 ;;
  esac
done

echo "==> doc2md dependency installer"
echo ""

# ── 1. Python core package ────────────────────────────────────────────────────
echo "[1/4] Python package (core + modern extras)"
pipx
 install -e ".[modern]"

# ── 2. System binaries via Homebrew ───────────────────────────────────────────
if [[ $SKIP_BREW -eq 0 ]]; then
  if command -v brew &>/dev/null; then
    echo "[2/4] Homebrew: poppler (pdftotext), tesseract (OCR), pandoc"
    brew install poppler tesseract pandoc
  else
    echo "[2/4] Homebrew not found — skipping system binaries."
    echo "      Install manually: poppler, tesseract, pandoc"
  fi
else
  echo "[2/4] --no-brew set, skipping Homebrew packages"
fi

# ── 3. Rust/Cargo parsers ─────────────────────────────────────────────────────
if [[ $SKIP_CARGO -eq 0 ]]; then
  if command -v cargo &>/dev/null; then
    echo "[3/4] Cargo: pdf-inspector, unpdf-cli, undoc-cli"
    cargo install pdf-inspector
    cargo install unpdf-cli
    cargo install undoc-cli
  else
    echo "[3/4] cargo not found — skipping Rust parsers."
    echo "      Install Rust from https://rustup.rs then re-run."
  fi
else
  echo "[3/4] --no-cargo set, skipping Cargo packages"
fi

# ── 4. MinerU (optional, heavy) ───────────────────────────────────────────────
if [[ $INSTALL_MINERU -eq 1 ]]; then
  echo "[4/4] MinerU — deep-learning PDF extraction (magic-pdf[full])"
  echo "      This installs PaddleOCR + layout models and downloads ~2 GB of weights."

  # pydantic-core <2.28 uses pyo3 ≤0.22 which only supports CPython ≤3.13.
  # On Python 3.14+ we must either use the ABI3 forward-compat flag or a newer
  # pydantic-core.  Try the newer pydantic-core first; fall back to the flag.
  PY_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
  PY_MINOR=$(python3 -c "import sys; print(sys.version_info.minor)")
  PY_MAJOR=$(python3 -c "import sys; print(sys.version_info.major)")

  if [[ $PY_MAJOR -ge 3 && $PY_MINOR -ge 14 ]]; then
    echo "      Detected Python $PY_VERSION — setting PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1"
    echo "      to allow pydantic-core to build against Python 3.14+."
    export PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1
  fi

  pipx install "magic-pdf[all]"
  echo ""
  echo "      Triggering first-run model download (this may take several minutes)..."
  # magic-pdf downloads weights on first invocation; --help triggers the check
  magic-pdf --help > /dev/null 2>&1 || true
  echo "      MinerU ready. Use: /doc2md --mineru  or  Engine('raw', 'sources', mineru=True)"
else
  echo "[4/4] MinerU skipped (pass --mineru to include it)"
  echo "      When needed: pip install magic-pdf[full]"
fi

echo ""
echo "Done. Verify with:  doc2md parsers"
