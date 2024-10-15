from playwright.sync_api import Page, expect
import allure


class PageActions:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url):
        with allure.step(f"Redirect to URL: {url}"):
            self.page.goto(url)

    def check_url(self, expected_url):
        with allure.step(f"URL check: expected URL - {expected_url}"):
            expect(self.page).to_have_url(expected_url)

    def wait_for_url_change(self, expected_url):
        with allure.step(f"Waiting for the URL to change to {expected_url}"):
            self.page.wait_for_url(expected_url)

    def wait_for_page_load(self):
        with allure.step(f"Waiting for the page to load"):
            self.page.wait_for_load_state('load')

    def click_button(self, selector):
        with allure.step(f"Click on the element: {selector}"):
            self.page.click(selector)

    def is_element_present(self, selector):
        with allure.step(f"Checking element visibility: {selector}"):
            expect(self.page.locator(selector)).to_be_visible()

    def is_button_active(self, selector):
        with allure.step(f"Checking button activity: {selector}"):
            expect(self.page.locator(selector)).to_be_enabled()

    def input_text(self, selector, text):
        with allure.step(f"Entering text  '{text}' into the element: {selector}"):
            self.page.fill(selector, text)

    def input_filtred_text(self, selector, text):
        with allure.step(f"Entering text ‘FILTRED’ into the element: {selector}"):
            self.page.fill(selector, text)

    def wait_for_selector(self, selector, timeout=1000):
        with allure.step(f"Waiting for the selector to appear: {selector}"):
            self.page.wait_for_selector(selector, state='visible', timeout=timeout)

    def wait_for_disappear_selector(self, selector, timeout=1000):
        with allure.step(f"Waiting for the selector to disappear: {selector}"):
            self.page.wait_for_selector(selector, state='detached', timeout=timeout)

    def assert_text_present_on_page(self, text):
        with allure.step(f"Checking for the presence of the text '{text}'on the page"):
            expect(self.page).to_have_text(text)

    def assert_text_in_element(self,selector, text):
        with allure.step(f"Checking for the presence of the text '{text}'in the element {selector}"):
            expect(self.page).locator(selector).to_have_text(text)

    def assert_element_attribute(self, selector, attribute, value):
        with allure.step(f"Checking the value '{value}' attribute '{attribute}' of the element’s {selector}"):
            expect(self.page).locator(selector).to_have_attribute(attribute, value)

    def assert_element_hidden(self, selector):
        with allure.step(f"Checking that the element {selector} is hidden"):
            expect(self.page).locator(selector).to_be_hidden()


