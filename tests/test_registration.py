import pytest
from pages.register_page import RegisterPage
from utils.test_data import REGISTRATION_USER


@pytest.mark.parametrize("case", range(7))
def test_registration_scenarios(page, base_url, case):
    register = RegisterPage(page, base_url); register.navigate()
    assert page.get_by_role("heading", name="Create your account").is_visible()
    data = REGISTRATION_USER.copy()
    if case == 0: return
    if case == 1: data["email"] = "new-unique@example.test"
    if case == 2: data["name"] = ""
    if case == 3: data["email"] = "bad-address"
    if case == 4: data["password"] = "short"
    if case == 5: data["confirm"] = "different"
    if case == 6: data["email"] = "alex@example.com"
    register.submit(data.get("name", ""), data.get("email", ""), data.get("password", ""), data.get("confirm", data.get("password", "")))
    if case == 1: assert "successfully" in register.message()
    elif case == 2: assert "required" in register.message()
    elif case == 3: assert "valid email" in register.message()
    elif case == 4: assert "8 characters" in register.message()
    elif case == 5: assert "do not match" in register.message()
    else: assert "already exists" in register.message()
