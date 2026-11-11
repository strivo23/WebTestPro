from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_dashboard_profile_and_logout(page, base_url, test_user):
    login = LoginPage(page, base_url); login.navigate(); login.submit(test_user["email"], test_user["password"])
    dashboard = DashboardPage(page, base_url)
    assert dashboard.welcome.inner_text() == "Welcome back, Alex"
    assert dashboard.profile_email.inner_text() == test_user["email"]
    dashboard.logout()
    assert page.url.endswith("login.html")
