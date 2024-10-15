import allure
from pages.base_page import BasePage

class LoginFragment(BasePage):
    def __init__(self, page):
        self.page = page
        super().__init__(page)
        self.create_from_url_selector = "a.createOption:has-text('From a repository URL')"
        self.create_manually_selector = "a.createOption:has-text(' Manually')"
