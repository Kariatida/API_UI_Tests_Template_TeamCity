import allure

from playwright.sync_api import Page, expect
from actions.page_actions import PageActions
from components.header import Header
from enums.hosts import BASE_URL


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self._base_url = BASE_URL
        self._endpoint = ""
        self.actions = PageActions(page)
        self.header = Header(self.actions)

    @property
    def page_url(self):
        return self._base_url + self._endpoint

    @page_url.setter
    def page_url(self, endpoint):
        self._endpoint = endpoint