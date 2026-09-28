import pytest
from pages.home_page import HomePage

@pytest.mark.ui
@pytest.mark.smoke
def test_search_product(page, base_url):
    page.goto(base_url)
    home = HomePage(page)
    home.search_product("Laptop")
    home.assert_product_visible("Laptop Pro")

@pytest.mark.ui
def test_add_to_cart_requires_login(page, base_url):
    page.goto(base_url)
    home = HomePage(page)
    home.add_first_product()
    assert home.checkout_button.is_disabled()

@pytest.mark.ui
@pytest.mark.smoke
def test_checkout_flow(logged_in_page):
    home = HomePage(logged_in_page)
    home.add_first_product()
    home.checkout()
    home.assert_order_success()
