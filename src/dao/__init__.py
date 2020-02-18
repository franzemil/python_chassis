from injector import inject, Module, provider, singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base

from services.config import AppConfiguration

class Database:
    @inject
    def __init__(self, app_config: AppConfiguration):
        self._database_uri = app_config.database_uri
        self._engine = create_engine(self._database_uri)

    @property
    def session(self) -> Session:
        session = sessionmaker(bind=self._engine)
        return session()

Base = declarative_base()