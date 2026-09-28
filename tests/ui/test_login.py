import pytest
from pages.login_page import LoginPage
from utils.config import settings

@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login(page, base_url):
    login = LoginPage(page)
    login.open(base_url)
    login.login(settings.test_email, settings.test_password)
    login.assert_success()

@pytest.mark.ui
@pytest.mark.parametrize("password", ["wrong", "", "bad-password"])
def test_invalid_login(page, base_url, password):
    login = LoginPage(page)
    login.open(base_url)
    login.login(settings.test_email, password)
    login.assert_error("Invalid credentials")
