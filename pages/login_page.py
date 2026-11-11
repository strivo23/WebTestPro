"""Login workflow page object."""
from .base_page import BasePage


class LoginPage(BasePage):
    def navigate(self): self.open("login.html")
    def submit(self, email: str, password: str):
        self.page.locator("#email").fill(email); self.page.locator("#password").fill(password); self.page.get_by_role("button", name="Log in").click()
    def error(self) -> str: return self.page.locator(".message").inner_text()
