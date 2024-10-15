from actions.page_actions import PageActions
from async_timeout import timeout

class Loading:
    def __init__(self, actions: PageActions):
        self.actions = actions
        self.loading_selector = '#stageDescription'

    def wait_loading(self, timeout=240000):
        self.actions.wait_for_selector(self.loading_selector, timeout=timeout)
        self.actions.wait_for_disappear_selector(self.loading_selector, timeout=timeout)

