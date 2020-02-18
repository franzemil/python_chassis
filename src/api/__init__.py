from flask import Flask, Config
from flask.views import View
from flask_injector import FlaskInjector
from services import UserService
from injector import singleton, Binder, inject, Module, provider
from dao.models import User
from services.config import AppConfiguration
from flask_restplus import Api, Resource, fields

class AppModule(Module):
    @provider
    @singleton
    def configuration(self, app: Flask) -> AppConfiguration:
        return AppConfiguration('sdfa1321121211s', 'sadsdfasfas', 'postgresql://postgres:@localhost:5432/mopsv_db')

class TodoResource(Resource):
    @inject
    def __init__(self, user_service: UserService, **kwargs):
        super().__init__(**kwargs)
        self._user_service = user_service

    def get(self, **kwargs):
        print(self._user_service.create_user(User('franz1232ssssss132132assdafsafadsfsa', 'Emil')))
        print(kwargs)
        return 'Hola'


def create_app():
    app = Flask(__name__)
    app.config.update(A='B')
    api = Api(app)
    api.add_resource(TodoResource, '/todo')
    FlaskInjector(app=app, modules=[AppModule])
    return app
