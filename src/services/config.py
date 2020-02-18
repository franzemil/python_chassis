from injector import inject


class AppConfiguration:
    @inject
    def __init__(self, secret_key: str, hash_key: str, database_uri: str):
        self._secret_key = secret_key
        self._hash_key = hash_key
        self._database_uri = database_uri

    @property
    def secret_key(self) -> str:
        return self._secret_key

    @property
    def hash_key(self) -> str:
        return self._hash_key

    @property
    def database_uri(self) -> str:
        return self._database_uri