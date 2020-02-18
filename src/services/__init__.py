from injector import inject

from dao.repositories import UserRepository, TokenRepositoty
from dao.models import User, Token
from .utils import TokenGenerator, CryptoUtils


class UserService:
    @inject
    def __init__(self, user_repository: UserRepository, hash_utils: CryptoUtils):
        self._user_repository = user_repository
        self._hash_utils = hash_utils

    def create_user(self, user: User) -> User:
        user.password = self._hash_utils.hash(user.password)
        user_created = self._user_repository.create(user)
        return user_created

class AuthenticationService:
    @inject
    def __init__(self, user_repository: UserRepository, token_repository: TokenRepositoty, token_generator: TokenGenerator, crypto_utils: CryptoUtils):
        self._user_repository = user_repository
        self._token_repository = token_repository
        self._token_generator = token_generator
        self._crypto_utils = crypto_utils

    def create_token(self, username: str, password: str) -> Token:
        user = self._user_repository.get_by_username(username)
        if self._crypto_utils.hash(password) == user.password:
            token = Token(user_id=user.id, token=self._token_generator.generate(user))
            return self._token_repository.create(token)
        return None

