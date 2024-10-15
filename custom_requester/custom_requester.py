import os
import logging

from enums.hosts import BASE_URL
from http import HTTPStatus


class CustomRequester:
    base_headers = dict({"Content-Type": "application/json", "Accept": "application/json"})

    def __init__(self, session):
        self.session = session
        self.base_url = BASE_URL
        self.logger = logging.getLogger(__name__)

    def send_request(self, method, endpoint, data=None, expected_status=HTTPStatus.OK, need_logging=True):
        """
        Wrapper for requests. Allows adding various logic.
        :param method: Request method
        :param endpoint: Endpoint to concatenate with BASE_URL in the "url" variable
        :param data: Request body. Defaults to empty to handle NO_CONTENT responses
        :param expected_status: Expected response status. If a status other than SC_OK is expected, pass it in the API class method
        :param need_logging: Flag for enabling logging. Default is True
        :return: Returns the response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, json=data)
        if need_logging:
            self.log_request_and_response(response)
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}")
        return response

    def _update_session_headers(self, **kwargs):
        self.headers = self.base_headers.copy()
        self.headers.update(kwargs)
        self.session.headers.update(self.headers)


    def log_request_and_response(self, response):
        """
        Logging of requests and responses. Logging settings are described in pytest.ini.
        Transforms the output into a curl-like format (-H for headers), (-d for body).
        :param response: Response object received from the "send_request" method
        """
        try:
            request = response.request
            GREEN = '\033[32m'
            RED = '\033[31m'
            RESET = '\033[0m'
            headers = " \\\n".join([f"-H '{header}: {value}'" for header, value in request.headers.items()])
            full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace(' (call)', '')}"

            body = ""
            if hasattr(request, 'body') and request.body is not None:
                if isinstance(request.body, bytes):
                    body = request.body.decode('utf-8')
                body = f"-d '{body}' \n" if body != '{}' else ''

            self.logger.info(
                f"{GREEN}{full_test_name}{RESET}\n"
                f"curl -X {request.method} '{request.url}' \\\n"
                f"{headers} \\\n"
                f"{body}"
            )

            response_status = response.status_code
            is_success = response.ok
            response_data = response.text
            if not is_success:
                self.logger.info(f"\tRESPONSE:"
                                 f"\nSTATUS_CODE: {RED}{response_status}{RESET}"
                                 f"\nDATA: {RED}{response_data}{RESET}")
        except Exception as e:
            self.logger.info(f"\nLogging went wrong: {type(e)} - {e}")