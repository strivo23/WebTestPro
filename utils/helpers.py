"""Small shared helpers for test infrastructure."""
import re
from datetime import datetime


def safe_filename(value: str) -> str:
    """Return a filesystem-safe, timestamped artifact name."""
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_")[:120]
    return f"{slug}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
