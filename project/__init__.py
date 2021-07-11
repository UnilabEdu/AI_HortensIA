import os
from project.config import Config
from flask import Flask, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from project.models.user import User
from flask_mail import Mail, Message
from flask_user import SQLAlchemyAdapter, UserManager
from project.models import db
from project.user.admin.admin import admin
from flask_migrate import Migrate
from flask_babel import Babel
from flask_restful import Api
from project.resources.emotions import EmotionList

migrate = Migrate()
babel = Babel()
mail = Mail()
api = Api()


def create_app(import_blueprints=True):
    app = Flask(__name__)
    app.config.from_object(Config)
    # database init
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    # flask-user init
    db_adapter = SQLAlchemyAdapter(db, User)  # Setup the SQLAlchemy DB Adapter
    UserManager(db_adapter, app)  # Init Flask-User and bind to app
    # flask-mail init
    mail.init_app(app)
    # flask-babel init
    babel.init_app(app)
    # flask-admin init
    admin.init_app(app)

    # TODO: remove import_blueprints (it's required for testing data_processing.py functions)
    if import_blueprints:
        # Blueprint registrations
        from project.dashboard.views import dashboard_blueprint
        app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

        from project.front_integration.views import homepage_blueprint
        app.register_blueprint(homepage_blueprint, url_prefix="/")

    from project.tickets.views import tickets_blueprint
    app.register_blueprint(tickets_blueprint, url_prefix="/tickets")

    # restful api
    api.init_app(app)
    api.add_resource(EmotionList, "/")

    return app
