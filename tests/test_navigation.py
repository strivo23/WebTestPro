import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.parametrize("case", range(5))
def test_navigation_and_session(page, base_url, test_user, case):
    page.goto(base_url)
    if case == 0:
        page.get_by_role("link", name="Log in").click(); assert page.url.endswith("login.html")
    elif case == 1:
        page.get_by_role("link", name="Create account").click(); assert page.url.endswith("register.html")
    else:
        dashboard = DashboardPage(page, base_url); dashboard.navigate()
        if case == 4:
            assert page.url.endswith("login.html")
        else:
            login = LoginPage(page, base_url); login.navigate(); login.submit(test_user["email"], test_user["password"])
            assert page.url.endswith("dashboard.html")
            if case == 3:
                DashboardPage(page, base_url).logout(); assert page.url.endswith("login.html")
