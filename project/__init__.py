from flask import Flask
from flask_user import SQLAlchemyAdapter, UserManager
from project.extensions import extensions_list, extensions_db_list
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


def register_blueprints(app):
    from project.main.views import homepage_blueprint
    app.register_blueprint(homepage_blueprint, url_prefix="/")

    from project.dashboard.views import dashboard_blueprint
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

    from project.tickets.views import tickets_blueprint
    app.register_blueprint(tickets_blueprint, url_prefix="/tickets")

    from project.Oauth import google_blueprint
    app.register_blueprint(google_blueprint, url_prefix="/login")


def register_commands(app):
    from project.commands import command_list

    for command in command_list:
        app.cli.add_command(command)


def create_app():
    """Create app instance."""
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)

    db_adapter = SQLAlchemyAdapter(db, User)  # Setup the SQLAlchemy DB Adapter
    UserManager(db_adapter, app)  # Init Flask-User and bind to app

    # Flask-Admin init
    admin.init_app(app)

    register_blueprints(app)
    register_commands(app)

    return app
