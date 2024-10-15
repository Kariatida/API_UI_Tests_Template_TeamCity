from actions.page_actions import PageActions

class FirstStartWindow:
    def __init__(self, actions: PageActions):
        self.actions = actions
        self.proceed_button_selector = '#proceedButton'

    def proceed_step(self):
        self.actions.is_element_present(self.proceed_button_selector)
        self.actions.is_button_active(self.proceed_button_selector)
        self.actions.click_button(self.proceed_button_selector)
        self.actions.wait_for_page_load()