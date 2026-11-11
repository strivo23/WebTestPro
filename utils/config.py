"""Central configuration for local runs and CI."""
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
APP_DIR = ROOT_DIR / "app"
BASE_URL = os.getenv("WEBTESTPRO_BASE_URL", "http://127.0.0.1:8000")
TIMEOUT_MS = int(os.getenv("WEBTESTPRO_TIMEOUT_MS", "10000"))
HEADLESS = os.getenv("WEBTESTPRO_HEADED", "0") != "1"
SCREENSHOT_DIR = ROOT_DIR / "screenshots"
REPORT_DIR = ROOT_DIR / "reports"
