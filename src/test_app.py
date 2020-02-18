from injector import singleton, Binder, Injector
from services.config import AppConfiguration
from dao import Database
from services import UserService
from sqlalchemy.orm.session import Session
from services.utils import TokenGenerator
from dao.models import User


def build_configuration(binder: Binder):
    configuration = AppConfiguration('123jashdflakj', '12321', 'postgresql://postgres:@localhost:5432/mopsv_db')
    binder.bind(AppConfiguration, to=configuration, scope=singleton)
    # binder.bind(Session, to=Database(configuration).session)


injector = Injector([build_configuration])


def build_application(configuration: AppConfiguration) -> Injector:
    def build_configuration(binder: Binder):
        binder.bind(AppConfiguration, to=configuration, scope=singleton)
    # binder.bind(Session, to=Database(configuration).session)
    return Injector([build_configuration])


# token_generator: TokenGenerator = injector.get(TokenGenerator)

# user_service: UserService = injector.get(UserService)

# user = user_service.create_user(User('franzemil', 'emil'))

# token = token_generator.generate(user)

# print(token)
# print(user.id)

