from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.place_order_button = page.get_by_role("button", name="Place order")

    def checkout(self):
        self.checkout_button.click()

    def place_order(self):
        self.place_order_button.click()

    def assert_order_created(self):
        expect(self.page.get_by_text("Order created", exact=False)).to_be_visible()
