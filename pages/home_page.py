from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_placeholder("Search products")
        self.search_button = page.get_by_role("button", name="Search")
        self.product_cards = page.locator("[data-testid='product-card']")

    def open(self, base_url: str):
        self.page.goto(base_url)

    def search(self, text: str):
        self.search_input.fill(text)
        self.search_button.click()

    def assert_product_visible(self, name: str):
        expect(self.page.get_by_text(name, exact=True)).to_be_visible()
