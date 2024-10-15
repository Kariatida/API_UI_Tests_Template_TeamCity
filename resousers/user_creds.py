import os
from dotenv import load_dotenv

load_dotenv()

class SuperAdminCreds:
    """
    Super admin credentials. For authorization in TeamCity as a super admin,
    the username is left empty, and the password is a token from the container logs.
    """
    USERNAME = ''
    PASSWORD = os.getenv('SUPER_USER_TOKEN')