import pytest
import allure

from data.project_data import ProjectResponseModel


class TestProjectCreate:

    @allure.feature('Project management')
    @allure.story('Project creation')
    @allure.testcase('https://testcase.manager/testcase/456', name='Test case')
    @allure.title('Project creation check')
    @allure.description('The test verifies the creation of a new project and its appearance in the general project list')
    def test_create_project(self, super_admin, project_data):
        project_data_1 = project_data()
        with allure.step('Sending a project creation request'):
            response = super_admin.api_manager.project_api.create_project(project_data_1.model_dump()).text
            project_response = ProjectResponseModel.model_validate_json(response)
        with pytest.assume:
            assert project_response.id == project_data_1.id
        with pytest.assume:
            assert project_response.parentProjectId == project_data_1.parentProject["locator"]
        with allure.step("Sending a request to retrieve information about the created project"):
            response = super_admin.api_manager.project_api.get_project_by_locator(project_data_1.name).text
        with allure.step("Checking the consistency of the created project’s parameters with the submitted data"):
            created_project = ProjectResponseModel.model_validate_json(response)
        with pytest.assume:
            assert created_project.id == project_data_1.id, \
                f"expected project id= {project_data_1.id}, but '{created_project.id}' given"

    def test_create_project_with_role(self, super_admin, project_data):
        project_data_1 = project_data()
        response = super_admin.api_manager.project_api.create_project(project_data_1.model_dump()).text
        project_response = ProjectResponseModel.model_validate_json(response)
        with pytest.assume:
            assert project_response.id == project_data_1.id, \
                f"expected project id= {project_data_1.id}, but '{project_response.id}' given"
            assert project_response.parentProjectId == project_data_1.parentProject["locator"], \
                (f"expected parent project id= {project_data_1.parentProject['locator']},"
                 f" but '{project_response.parentProjectId}' given in response")


