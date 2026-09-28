from pathlib import Path
import pytest
from playwright.sync_api import Page
from utils.config import settings
from utils.logger import get_logger
from database.db_client import DatabaseClient

logger = get_logger(__name__)
pytest_plugins = ["fixtures.api_fixtures"]

@pytest.fixture(scope="session")
def base_url():
    return settings.base_url

@pytest.fixture(scope="session")
def db():
    return DatabaseClient(settings.database_url)

@pytest.fixture
def logged_in_page(page: Page, base_url):
    from pages.login_page import LoginPage
    login = LoginPage(page)
    login.open(base_url)
    login.login(settings.test_email, settings.test_password)
    login.assert_success()
    return page

@pytest.fixture
def authenticated_user(auth_client):
    response = auth_client.login(settings.test_email, settings.test_password)
    assert response.status_code == 200
    return response.json()["user"]

@pytest.fixture
def first_product(product_client):
    response = product_client.list()
    assert response.status_code == 200
    products = response.json()
    assert products
    return products[0]

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
    if report.when == "call" and report.failed and settings.screenshot_on_failure:
        page = item.funcargs.get("page")
        if page:
            Path("reports/screenshots").mkdir(parents=True, exist_ok=True)
            safe_name = item.nodeid.replace("/", "_").replace("::", "_")
            page.screenshot(path=f"reports/screenshots/{safe_name}.png", full_page=True)
