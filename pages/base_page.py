"""Shared browser actions for page objects."""
import logging
from playwright.sync_api import Page

LOGGER = logging.getLogger(__name__)


class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url.rstrip("/")

    def open(self, path: str = "") -> None:
        url = f"{self.base_url}/{path.lstrip('/')}"
        LOGGER.info("Navigating to %s", url)
        self.page.goto(url, wait_until="domcontentloaded")

    def text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()
