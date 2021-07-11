# App settings

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    APP_NAME = "Hortensia"

    # Flask settings
    CSRF_ENABLED = True
    PROPAGATE_EXCEPTIONS = True

    # Flask SQLAlchemy settings
    SECRET_KEY = "Cannottell"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask mail configuration
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '630ddbfbb61f3c'
    MAIL_PASSWORD = '18f185a477f02f'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # Flask-User settings
    USER_ENABLE_EMAIL = True
    USER_ALLOW_LOGIN_WITHOUT_CONFIRMED_EMAIL = False
    USER_SEND_REGISTERED_EMAIL = True
    USER_AUTO_LOGIN_AT_LOGIN = True
    USER_AUTO_LOGIN_AFTER_CONFIRM = True

    USER_LOGIN_TEMPLATE = 'flask_user/login_or_register.html'
    USER_REGISTER_TEMPLATE = 'flask_user/login_or_register.html'

    USER_ENABLE_RETYPE_PASSWORD = False

    LANGUAGES = {
        "en": "English",
        "ka": "Georgian"
    }
