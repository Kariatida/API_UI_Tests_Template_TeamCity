import allure

from pages.setup_page import SetUpPage


@allure.title("Server setup")
@allure. description("Setting up the reception provider")
def test_set_up(browser):
    with allure.step("Setup"):
        set_up_page = SetUpPage(browser)

        set_up_page.set_up()