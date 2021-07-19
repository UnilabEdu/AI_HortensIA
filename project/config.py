# App settings

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    APP_NAME = "Hortensia"

    # Flask settings
    CSRF_ENABLED = True
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = "Cannottell"  # TODO: move secret key to environmental variables

    # Flask SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # TODO: configure to unilab mail
    # Flask mail configuration
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '02f8e167040c3d'
    MAIL_PASSWORD = 'eb53bb82c96877'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = 'denissanturyan@gmail.com'

    # Flask-User settings
    USER_ENABLE_EMAIL = True
    USER_ALLOW_LOGIN_WITHOUT_CONFIRMED_EMAIL = False
    USER_SEND_REGISTERED_EMAIL = True
    USER_AUTO_LOGIN_AT_LOGIN = True
    USER_AUTO_LOGIN_AFTER_CONFIRM = True

    USER_REGISTER_URL = '/register'
    USER_LOGIN_URL = '/'

    USER_LOGIN_TEMPLATE = 'flask_user/login_or_register.html'
    USER_REGISTER_TEMPLATE = 'flask_user/login_or_register.html'

    USER_AFTER_LOGIN_ENDPOINT = 'tickets.tickets'

    USER_ENABLE_RETYPE_PASSWORD = False

    LANGUAGES = {
        "en": "English",
        "ka": "Georgian"
    }

    BABEL_DEFAULT_LOCALE = 'ka'
    BABEL_DOMAIN = 'messages'
