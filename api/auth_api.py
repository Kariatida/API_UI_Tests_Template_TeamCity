from custom_requester.custom_requester import CustomRequester
from enums.hosts import BASE_URL


class AuthAPI(CustomRequester):

    def auth_and_get_csrf(self, user_creds):
        self.session.auth = user_creds
        csrf_token = self.send_request("GET", "/authenticationTest.html?csrf").text
        if not csrf_token:
                raise ValueError("CSRF Token is missing or invalid")
        self._update_session_headers(**{"X-TC-CSRF-Token": csrf_token})

