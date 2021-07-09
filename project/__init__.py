import os
from project.config import Config
from flask import Flask, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from project.models.user import UserModel
from flask_mail import Mail, Message
from flask_user import SQLAlchemyAdapter, UserManager
from project.models import db
from project.user.admin.admin import admin
from flask_migrate import Migrate
from flask_babel import Babel

migrate = Migrate()
babel = Babel()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # database init
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    # flask-user init
    db_adapter = SQLAlchemyAdapter(db, UserModel)  # Setup the SQLAlchemy DB Adapter
    UserManager(db_adapter, app)  # Init Flask-User and bind to app
    # flask-mail init
    mail.init_app(app)
    # flask-babel init
    babel.init_app(app)
    # flask-admin init
    admin.init_app(app)

    # Blueprint registrations
    from project.front_integration.views import homepage_blueprint
    app.register_blueprint(homepage_blueprint, url_prefix="/")


    return app
