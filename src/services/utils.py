import jwt
from injector import inject

from dao.models import User
from .config import AppConfiguration

class TokenGenerator:
    @inject
    def __init__(self, app_configuration: AppConfiguration):
        self._app_configuration = app_configuration

    def generate(self, user: User) -> str:
        return jwt.encode({'id': user.id, 'username': user.username}, self._app_configuration._secret_key, algorithm='HS256')

class CryptoUtils:
    @inject
    def __init__(self, app_configuration: AppConfiguration):
        self.app_configuration = app_configuration

    def hash(self, value: str) -> str:
        return '12313123213'