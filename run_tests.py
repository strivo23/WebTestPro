"""Start the local demo app and run pytest with an HTML report."""
import os
import subprocess
import sys
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from functools import partial
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from utils.config import APP_DIR, BASE_URL, REPORT_DIR  # noqa: E402


def main():
    REPORT_DIR.mkdir(exist_ok=True)
    server = ThreadingHTTPServer(("127.0.0.1", 8000), partial(SimpleHTTPRequestHandler, directory=str(APP_DIR)))
    thread = threading.Thread(target=server.serve_forever, daemon=True); thread.start()
    time.sleep(0.3)
    command = [sys.executable, "-m", "pytest", "--html=reports/report.html", "--self-contained-html", *sys.argv[1:]]
    env = os.environ.copy(); env.setdefault("WEBTESTPRO_BASE_URL", BASE_URL)
    try:
        result = subprocess.run(command, cwd=ROOT, env=env, check=False)
        print(f"\nReport: {REPORT_DIR / 'report.html'}")
        return result.returncode
    finally:
        server.shutdown(); server.server_close()


if __name__ == "__main__": raise SystemExit(main())
