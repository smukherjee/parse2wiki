"""qpdf integration — detect and decrypt password-protected PDFs.

Detection prefers ``qpdf --requires-password``, which distinguishes three
cases in one call: not encrypted, encrypted-but-empty-user-password (owner
lock only — no prompt needed), and a real password required. When qpdf isn't
installed, a byte-level ``/Encrypt`` scan is used as a best-effort fallback so
a locked PDF still surfaces a clear warning instead of failing silently
deeper in the parser chain.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Literal, Optional

QPDF_INSTALL_HINT = (
    "qpdf not found — password-protected PDFs cannot be decrypted.\n"
    "  macOS:   brew install qpdf\n"
    "  Ubuntu:  sudo apt install qpdf\n"
)

PasswordStatus = Literal["none", "owner-only", "required", "unknown"]

# qpdf --requires-password exit codes (see `qpdf --help=--requires-password`):
#   0 = a password other than the one supplied is required
#   2 = the file is not encrypted
#   3 = encrypted, but the supplied (here: empty) password is correct
_REQUIRES_PASSWORD_STATUS: dict[int, PasswordStatus] = {
    0: "required",
    2: "none",
    3: "owner-only",
}


def qpdf_available() -> bool:
    return shutil.which("qpdf") is not None


def looks_encrypted(path: str) -> bool:
    """Best-effort byte scan for a PDF ``/Encrypt`` trailer entry.

    Only meaningful when qpdf isn't installed — a heuristic so a locked PDF
    still gets flagged instead of failing silently later in the chain.
    """
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError:
        return False
    return b"/Encrypt" in data


def password_status(path: str, timeout: int = 30) -> PasswordStatus:
    """Classify a PDF's password requirement without needing the password."""
    if not qpdf_available():
        return "unknown"
    try:
        proc = subprocess.run(
            ["qpdf", "--requires-password", path],
            capture_output=True, text=True, timeout=timeout,
        )
    except (subprocess.TimeoutExpired, OSError):
        return "unknown"
    return _REQUIRES_PASSWORD_STATUS.get(proc.returncode, "unknown")


def decrypt_pdf(path: str, password: str, dest: str, timeout: int = 60) -> tuple[bool, Optional[str]]:
    """Write a password-stripped copy of ``path`` to ``dest``.

    Returns ``(True, None)`` on success, ``(False, message)`` otherwise —
    e.g. ``"invalid password"`` when ``password`` is wrong.
    """
    Path(dest).parent.mkdir(parents=True, exist_ok=True)
    try:
        proc = subprocess.run(
            ["qpdf", f"--password={password}", "--decrypt", path, dest],
            capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return False, "qpdf timed out"
    except OSError:
        return False, "qpdf not on PATH"
    if proc.returncode != 0:
        err = (proc.stderr or "").strip().splitlines()
        msg = err[-1].split(": ", 1)[-1] if err else f"qpdf exit {proc.returncode}"
        return False, msg
    return True, None
