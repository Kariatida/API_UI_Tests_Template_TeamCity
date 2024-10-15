
from components.agreement import Agreement
from components.first_start_window import FirstStartWindow
from components.loading import Loading
from components.setup_user import SetupUser
from enums.hosts import BASE_URL
from pages.base_page import BasePage

class SetUpPage(BasePage):
    page_url = BASE_URL

    def __init__(self, page):
        super().__init__(page)
        self.first_start_window = FirstStartWindow(self.actions)
        self.loading = Loading(self.actions)
        self.agreement = Agreement(self.actions)
        self.setup_user = SetupUser(self.actions)
        self.page_url = BASE_URL

    def set_up(self, username="admin", password="admin"):
        self.actions.navigate(self.page_url)
        self.actions.wait_for_page_load()
        self.first_start_window.proceed_step()
        self.loading.wait_loading()
        self.first_start_window.proceed_step()
        self.loading.wait_loading()
        self.actions.navigate(self.agreement.page_url)
        self.agreement.check_in_box()
        self.agreement.continue_agreement()
        self.actions.wait_for_page_load()
        self.setup_user.create_user(username, password)