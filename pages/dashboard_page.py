"""Dashboard and logout page object."""
from .base_page import BasePage


class DashboardPage(BasePage):
    def navigate(self): self.open("dashboard.html")
    @property
    def welcome(self): return self.page.locator("#welcome")
    @property
    def profile_email(self): return self.page.locator("#profile-email")
    def logout(self): self.page.get_by_role("button", name="Log out").click()
