from injector import inject
from . import Database
from sqlalchemy.orm.session import Session
from .models import User, Token


class AbastractRepository:
    @inject
    def __init__(self, db: Database):
        self._db = db

    def session(self) -> Session:
        return self._db.session

class UserRepository(AbastractRepository):
    def create(self, user: User) -> User:
        session = self.session()
        session.add(user)
        session.commit()
        return user

class TokenRepositoty(AbastractRepository):
    def create(self, token: Token):
        session = self.session()
        session.add(token)
        session.commit()
        return token