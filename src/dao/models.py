from sqlalchemy import Column, String, Integer, ForeignKey

from . import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(length=50), unique=True)
    password = Column(String(length=140))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    token = Column(String(length=255))

    def __init__(self, user_id: int, token: str):
        self.user_id = user_id
        self.token = token