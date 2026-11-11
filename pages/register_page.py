"""Registration workflow page object."""
from .base_page import BasePage


class RegisterPage(BasePage):
    def navigate(self): self.open("register.html")
    def submit(self, name="", email="", password="", confirm=""):
        for selector, value in (("#name", name), ("#email", email), ("#password", password), ("#confirm-password", confirm)):
            self.page.locator(selector).fill(value)
        self.page.get_by_role("button", name="Create account").click()
    def message(self) -> str: return self.page.locator(".message").inner_text()
