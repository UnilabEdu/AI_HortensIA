import os
from config import Config
from flask import Flask, render_template, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from project.models.user import UserModel
from flask_mail import Mail, Message
from flask_user import SQLAlchemyAdapter, UserManager
from project.models import db
from project.user.admin.admin import admin
from flask_migrate import Migrate

migrate = Migrate()


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
    mail = Mail(app)

    # flask-admin init
    admin.init_app(app)

    # Blueprint registrations
    from project.dashboard.views import dashboard_blueprint
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

    return app
