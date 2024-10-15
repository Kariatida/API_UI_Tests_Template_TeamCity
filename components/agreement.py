from actions.page_actions import PageActions
from enums.hosts import BASE_URL


class Agreement:
    def __init__(self, actions: PageActions):
        self.actions = actions
        self.page_url = f'{BASE_URL}/showAgreement'
        self.checkbox_selector = '#accept'
        self.continue_button_selector = '[type="submit"]'

    def check_in_box(self):
        self.actions.is_element_present(self.checkbox_selector)
        self.actions.click_button(self.checkbox_selector)

    def continue_agreement(self):
        self.actions.is_element_present(self.continue_button_selector)
        self.actions.is_button_active(self.continue_button_selector)
        self.actions.click_button(self.continue_button_selector)
        self.actions.wait_for_page_load()