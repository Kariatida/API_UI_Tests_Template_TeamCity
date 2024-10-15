from api.api_manager import ApiManager
from enums.roles import Roles


class Role:
    def __init__(self, role_id, scope="g", href=None):
        if role_id not in Roles.__members__:
            raise ValueError(f"Invalid role: {role_id}")
        self.role_id = role_id
        self.scope = scope
        self.href = href

class User:
    def __init__(self, username: str, password: str, session: ApiManager, roles: list, **kwargs):
        self.api_manager = session
        self.username = username
        self.password = password
        self.email = None
        self.roles = roles
        self.groups = None

    @property
    def creds(self):
        return self.username, self.password