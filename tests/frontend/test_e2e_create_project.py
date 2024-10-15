import time

import allure

from data.project_data import ProjectResponseModel
from pages.create_project_page import ProjectCreationPage


def test_e2e_create_project(project_data, browser, super_admin):
    project_data_1 = project_data()
    project_id = project_data_1.id
    project_name = project_data_1.name

    with allure.step("User authentication"):
        browser.goto('http://localhost:8111/login.html', timeout=60000)
        browser.fill('#username', 'admin')
        browser.fill('#password', 'admin')
        browser.wait_for_selector('.loginButton', timeout=30000)
        browser.click('.loginButton')
        browser.wait_for_url('http://localhost:8111/favorite/projects', timeout=60000)
    with allure.step("Project creation"):
        project_creation_browser = ProjectCreationPage(browser)
        project_creation_browser.create_project(project_name, project_id, project_name)
    with allure.step("Sending a request to retrieve information about the created project."):
        response = super_admin.api_manager.project_api.get_project_by_locator(project_data_1.name).text
        created_project = ProjectResponseModel.model_validate_json(response)
        assert created_project.id == project_data_1.id, \
            f"expected project id= {project_data_1.id}, but '{created_project.id}' given"
        project_creation_browser.header.go_to_projects_throw_header_button()
        time.sleep(2)