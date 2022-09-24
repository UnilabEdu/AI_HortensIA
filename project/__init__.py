from flask import Flask
from flask_babel import Babel
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_user import SQLAlchemyAdapter, UserManager

from project.admin.admin import admin
from project.config import Config
from project.models import db
from project.models.user import User


def register_extensions(app):
    """Register extensions"""

    for extension in extensions_list:
        extension.init_app(app)

    for db_extension in extensions_db_list:
        db_extension.init_app(app, db)

    # Blueprint registrations
    from project.main.views import homepage_blueprint
    app.register_blueprint(homepage_blueprint, url_prefix="/")

    from project.dashboard.views import dashboard_blueprint
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

    from project.tickets.views import tickets_blueprint
    app.register_blueprint(tickets_blueprint, url_prefix="/tickets")

    from project.Oauth import google_blueprint
    app.register_blueprint(google_blueprint, url_prefix="/login")

    return app
