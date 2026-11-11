import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.parametrize("case", range(8))
def test_login_scenarios(page, base_url, test_user, case):
    login = LoginPage(page, base_url); login.navigate()
    assert page.get_by_role("heading", name="Log in to your account").is_visible()
    if case == 0: return
    if case == 1:
        login.submit(test_user["email"], test_user["password"])
        assert page.url.endswith("dashboard.html")
    elif case == 2:
        login.submit(test_user["email"], "wrong-password")
        assert "incorrect" in login.error()
    elif case == 3:
        login.submit("bad-email", "anything")
        assert "valid email" in login.error()
    elif case == 4:
        login.submit("", test_user["password"])
        assert "required" in login.error()
    elif case == 5:
        login.submit(test_user["email"], "")
        assert "required" in login.error()
    elif case == 6:
        login.submit("", "")
        assert "required" in login.error()
    else:
        login.submit(test_user["email"], test_user["password"])
        dashboard = DashboardPage(page, base_url)
        assert dashboard.profile_email.inner_text() == test_user["email"]
