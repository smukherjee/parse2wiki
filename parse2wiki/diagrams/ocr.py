#!/usr/bin/env python3
"""
OCR utilities for diagram extraction.

Uses tesseract for text extraction from images/diagrams.
"""

import subprocess
import tempfile
from pathlib import Path
from typing import List, Optional


def run_tesseract(image_path: str, lang: str = "eng") -> str:
    """Run tesseract OCR on an image file."""
    try:
        result = subprocess.run(
            ["tesseract", image_path, "stdout", "-l", lang],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return "OCR timeout"
    except FileNotFoundError:
        return "Tesseract not found - run: brew install tesseract"
    except Exception as e:
        return f"OCR failed: {e}"


def extract_images_from_pdf(pdf_path: str, output_dir: str) -> List[str]:
    """Extract images from PDF for OCR processing."""
    try:
        from pdf2image import convert_from_path

        images = convert_from_path(pdf_path, dpi=300)
        image_paths = []

        for i, image in enumerate(images):
            image_path = f"{output_dir}/page_{i + 1}.png"
            image.save(image_path, "PNG")
            image_paths.append(image_path)

        return image_paths
    except ImportError:
        return []
    except Exception as e:
        print(f"Image extraction failed: {e}")
        return []


def ocr_pdf_with_diagrams(pdf_path: str, ocr_output_dir: str) -> dict:
    """
    Run OCR on PDF and detect diagram content.

    Returns:
        dict with page_number -> ocr_text mapping
    """
    from .detector import detect_diagrams

    image_paths = extract_images_from_pdf(pdf_path, ocr_output_dir)
    results = {}

    for image_path in image_paths:
        page_num = int(Path(image_path).stem.split('_')[1])
        ocr_text = run_tesseract(image_path)

        # Check if this page contains diagram content
        detection = detect_diagrams(ocr_text)

        results[page_num] = {
            'ocr_text': ocr_text,
            'has_diagram': detection.has_diagram,
            'complexity': detection.complexity,
            'image_path': image_path
        }

    return results


def preprocess_image_for_ocr(image_path: str) -> str:
    """
    Preprocess image for better OCR results.

    Uses ImageMagick if available.
    """
    try:
        # Convert to grayscale and increase contrast
        subprocess.run([
            "convert", image_path,
            "-colorspace", "Gray",
            "-contrast-stretch", "2%",
            "-sharpen", "0x1",
            image_path  # Overwrite in place
        ], check=True)
        return image_path
    except Exception:
        return image_path  # Return original if preprocessing fails
