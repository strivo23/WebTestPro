import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


@pytest.mark.parametrize("case", range(5))
def test_form_validation(page, base_url, case):
    if case < 2:
        form = LoginPage(page, base_url); form.navigate()
        form.submit("", "") if case == 0 else form.submit("not-an-email", "password")
        assert "required" in form.error() if case == 0 else "valid email" in form.error()
    else:
        form = RegisterPage(page, base_url); form.navigate()
        form.submit("Taylor", "taylor@example.test", "short" if case == 2 else "StrongPass123", "different" if case == 3 else ("short" if case == 2 else "StrongPass123"))
        assert ("8 characters" in form.message()) if case == 2 else ("do not match" in form.message()) if case == 3 else ("successfully" in form.message())
