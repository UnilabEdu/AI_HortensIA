# App settings

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config (object):
    APP_NAME = "Hortensia"

    #Flask settings
    CSRF_ENABLED = True


    #Flask SQLAlchemy settings
    SECRET_KEY = "Cannottell"
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "data.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    #Flask-User settings