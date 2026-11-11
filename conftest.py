"""Pytest fixtures, logging, isolation, and failure evidence."""
import logging
import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, HEADLESS, REPORT_DIR, SCREENSHOT_DIR, TIMEOUT_MS
from utils.test_data import VALID_USER
from utils.helpers import safe_filename


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    REPORT_DIR.mkdir(exist_ok=True); SCREENSHOT_DIR.mkdir(exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s", handlers=[logging.FileHandler(REPORT_DIR / "test_execution.log", encoding="utf-8"), logging.StreamHandler()], force=True)
    logging.getLogger(__name__).info("Test execution started")


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=HEADLESS)
        logging.getLogger(__name__).info("Chromium launched (headless=%s)", HEADLESS)
        yield browser
        browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page(); page.set_default_timeout(TIMEOUT_MS)
    yield page
    page.close()


@pytest.fixture(scope="session")
def base_url(): return BASE_URL


@pytest.fixture
def test_user(): return VALID_USER.copy()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            path = SCREENSHOT_DIR / f"{safe_filename(item.name)}.png"
            try:
                page.screenshot(path=str(path), full_page=True)
                logging.getLogger(__name__).error("Test failed; screenshot saved to %s", path)
                report.screenshot_path = str(path)
            except Exception:
                logging.getLogger(__name__).exception("Could not capture failure screenshot")
