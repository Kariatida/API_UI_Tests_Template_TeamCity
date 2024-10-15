from actions.page_actions import PageActions
from enums.hosts import BASE_URL


class SetupUser:
    def __init__(self, actions: PageActions):
        self.actions = actions
        self.username_input_selector = '#input_teamcityUsername'
        self.password_input_selector = '#password1'
        self.retyped_password_input_selector = '#retypedPassword'
        self.create_button_selector = '[type="submit"]'

    def create_user(self, username: str, password: str):
        self.actions.input_text(self.username_input_selector, username)
        self.actions.input_text(self.password_input_selector, password)
        self.actions.input_text(self.retyped_password_input_selector, password)
        self.actions.is_element_present(self.create_button_selector)
        self.actions.is_button_active(self.create_button_selector)
        self.actions.click_button(self.create_button_selector)
        self.actions.wait_for_page_load()