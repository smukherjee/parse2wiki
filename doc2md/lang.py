"""Language detection and extraction for multilingual documents.

Supports deterministic language identification and routing to appropriate
OCR engines for Arabic, Hindi, and other non-Latin scripts.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

try:
    from langdetect import detect, DetectorFactory
    from langdetect.lang_detect_exception import LangDetectException
    _HAS_LANGDETECT = True
    # Make detection deterministic
    DetectorFactory.seed = 42
except ImportError:
    _HAS_LANGDETECT = False


# Unicode ranges for common scripts
SCRIPT_RANGES = {
    "arabic": (0x0600, 0x06FF),      # Arabic
    "arabic_supplement": (0x0750, 0x077F),
    "arabic_extended_a": (0x08A0, 0x08FF),
    "devanagari": (0x0900, 0x097F),  # Hindi/Sanskrit
    "devanagari_extended": (0xA8E0, 0xA8FF),
    "bengali": (0x0980, 0x09FF),
    "cjk": (0x4E00, 0x9FFF),         # Chinese/Japanese
    "hangul": (0xAC00, 0xD7AF),      # Korean
    "hiragana": (0x3040, 0x309F),
    "katakana": (0x30A0, 0x30FF),
    "cyrillic": (0x0400, 0x04FF),
    "greek": (0x0370, 0x03FF),
    "hebrew": (0x0590, 0x05FF),
    "thai": (0x0E00, 0x0E7F),
}

# Language codes for Tesseract
TESS_LANGS = {
    "ar": "ara",       # Arabic
    "hi": "hin",       # Hindi (Devanagari)
    "bn": "ben",       # Bengali
    "zh": "chi_sim",   # Chinese (Simplified)
    "zh-tw": "chi_tra", # Chinese (Traditional)
    "ja": "jpn",       # Japanese
    "ko": "kor",       # Korean
    "ru": "rus",       # Russian (Cyrillic)
    "el": "ell",       # Greek
    "he": "heb",       # Hebrew
    "th": "tha",       # Thai
}


@dataclass
class ScriptDetection:
    """Result of script detection on a text sample."""
    script: str
    confidence: float
    char_count: int
    sample: str


@dataclass
class LanguageResult:
    """Language detection result."""
    language: str
    script: str
    confidence: float
    text_sample: str


def _count_script_chars(text: str, script_name: str) -> int:
    """Count characters belonging to a specific script."""
    ranges = SCRIPT_RANGES.get(script_name)
    if not ranges:
        return 0
    low, high = ranges
    count = 0
    for char in text:
        code = ord(char)
        if low <= code <= high:
            count += 1
    # Also check related ranges
    if script_name == "arabic":
        count += _count_script_chars(text, "arabic_supplement")
        count += _count_script_chars(text, "arabic_extended_a")
    elif script_name == "devanagari":
        count += _count_script_chars(text, "devanagari_extended")
    return count


def detect_script(text: str, min_chars: int = 10) -> list[ScriptDetection]:
    """Detect scripts present in text based on Unicode ranges.

    Returns list of ScriptDetection objects sorted by character count.
    """
    results = []
    text_len = len(text)

    for script_name in SCRIPT_RANGES:
        # Skip extended ranges for top-level detection
        if script_name.endswith("_supplement") or script_name.endswith("_extended"):
            continue

        count = _count_script_chars(text, script_name)
        if count >= min_chars:
            results.append(ScriptDetection(
                script=script_name,
                confidence=count / max(text_len, 1),
                char_count=count,
                sample=text[:100],
            ))

    return sorted(results, key=lambda x: x.char_count, reverse=True)


def detect_language(text: str, min_length: int = 20) -> LanguageResult:
    """Detect language of text using langdetect with script fallback.

    For short texts or texts with non-Latin scripts, uses script detection
    as a fallback.
    """
    text = text.strip()
    if len(text) < min_length:
        # Too short for reliable detection, use script detection
        scripts = detect_script(text, min_chars=3)
        if scripts:
            primary = scripts[0]
            # Map script to likely language
            script_lang_map = {
                "arabic": ("ar", "Arabic"),
                "devanagari": ("hi", "Hindi"),
                "bengali": ("bn", "Bengali"),
                "cjk": ("zh", "Chinese"),
                "hangul": ("ko", "Korean"),
                "hiragana": ("ja", "Japanese"),
                "katakana": ("ja", "Japanese"),
                "cyrillic": ("ru", "Russian"),
                "greek": ("el", "Greek"),
                "hebrew": ("he", "Hebrew"),
                "thai": ("th", "Thai"),
            }
            lang_code, lang_name = script_lang_map.get(
                primary.script, ("unknown", "Unknown")
            )
            return LanguageResult(
                language=lang_code,
                script=primary.script,
                confidence=primary.confidence,
                text_sample=text[:100],
            )
        return LanguageResult(
            language="unknown",
            script="unknown",
            confidence=0.0,
            text_sample=text[:100],
        )

    # Use langdetect for longer texts
    if _HAS_LANGDETECT:
        try:
            lang = detect(text)
            scripts = detect_script(text, min_chars=3)
            script = scripts[0].script if scripts else "latin"
            return LanguageResult(
                language=lang,
                script=script,
                confidence=0.9,
                text_sample=text[:100],
            )
        except LangDetectException:
            pass

    # Fallback to script detection
    scripts = detect_script(text, min_chars=3)
    if scripts:
        return LanguageResult(
            language="unknown",
            script=scripts[0].script,
            confidence=scripts[0].confidence,
            text_sample=text[:100],
        )

    return LanguageResult(
        language="en",
        script="latin",
        confidence=0.5,
        text_sample=text[:100],
    )


def split_by_language(text: str, min_segment: int = 50) -> list[tuple[str, str]]:
    """Split text into segments by language.

    Returns list of (language, text) tuples.
    Consecutive lines are grouped if they share the same language.
    """
    lines = text.split('\n')
    segments = []
    current_lang = None
    current_text = []

    for line in lines:
        if len(line.strip()) < min_segment:
            # Short line, keep with current segment
            if current_text:
                current_text.append(line)
            continue

        result = detect_language(line, min_length=20)
        lang = result.language

        if current_lang is None:
            current_lang = lang
            current_text = [line]
        elif lang == current_lang:
            current_text.append(line)
        else:
            # Language changed, emit segment
            if current_text:
                segments.append((current_lang, '\n'.join(current_text)))
            current_lang = lang
            current_text = [line]

    # Emit final segment
    if current_text:
        segments.append((current_lang, '\n'.join(current_text)))

    return segments


# Script to language code mapping
SCRIPT_TO_LANG = {
    "arabic": "ar",
    "devanagari": "hi",
    "bengali": "bn",
    "cjk": "zh",
    "hangul": "ko",
    "hiragana": "ja",
    "katakana": "ja",
    "cyrillic": "ru",
    "greek": "el",
    "hebrew": "he",
    "thai": "th",
}


def get_tesseract_lang(script: str) -> Optional[str]:
    """Get Tesseract language code for a script."""
    lang_code = SCRIPT_TO_LANG.get(script)
    if lang_code:
        return TESS_LANGS.get(lang_code)
    return None


def get_tesseract_langs_for_text(text: str) -> list[str]:
    """Get list of Tesseract language codes needed for text.

    Returns ['eng'] for Latin text, or ['eng', 'ara'] for mixed Arabic/Latin, etc.
    """
    scripts = detect_script(text, min_chars=5)
    langs = ["eng"]  # Always include English as fallback

    for s in scripts:
        if s.script != "latin":
            tess_lang = get_tesseract_lang(s.script)
            if tess_lang and tess_lang not in langs:
                langs.append(tess_lang)

    return langs


def has_non_latin_text(text: str, threshold: int = 10) -> bool:
    """Check if text contains significant non-Latin content."""
    scripts = detect_script(text, min_chars=threshold)
    if not scripts:
        return False
    # Check if primary script is non-Latin
    non_latin_scripts = set(SCRIPT_RANGES.keys()) - {"latin"}
    return scripts[0].script in non_latin_scripts


def extract_multilingual(text: str) -> dict:
    """Extract language metadata from text.

    Returns dict with:
        - primary_language: Most prevalent language code
        - languages: List of detected language codes
        - segments: Language-segmented text
        - script_info: Script detection results
    """
    scripts = detect_script(text)
    primary_script = scripts[0].script if scripts else "latin"

    result = detect_language(text)
    segments = split_by_language(text)

    return {
        "primary_language": result.language,
        "primary_script": primary_script,
        "languages": list(set(lang for lang, _ in segments)),
        "segments": segments,
        "script_info": [
            {"script": s.script, "count": s.char_count, "confidence": s.confidence}
            for s in scripts
        ],
        "tesseract_lang": get_tesseract_lang(primary_script),
    }
