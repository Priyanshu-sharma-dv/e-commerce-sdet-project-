import pytest
from pages.login_page import LoginPage
from utils.config import settings


@pytest.mark.ui
@pytest.mark.regression
def test_login_controls_have_accessible_names(page, base_url):
    login = LoginPage(page)
    login.open(base_url)
    assert page.get_by_label("Email").is_visible()
    assert page.get_by_label("Password").is_visible()
    assert page.get_by_role("button", name="Login").is_visible()
