from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.get_by_label("Email")
        self.password = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.message = page.locator("#loginMessage")

    def open(self, base_url: str):
        self.page.goto(base_url)

    def login(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()

    def assert_success(self):
        expect(self.message).to_have_text("Login successful")

    def assert_error(self, message: str):
        expect(self.message).to_have_text(message)
