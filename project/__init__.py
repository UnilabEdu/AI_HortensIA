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


migrate = Migrate()
babel = Babel()
mail = Mail()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # SQLAlchemy init
    db.init_app(app)

    # Flask-Migrate init
    migrate.init_app(app, db, render_as_batch=True)

    # Flask-User init
    login_manager.init_app(app)

    db_adapter = SQLAlchemyAdapter(db, User)  # Setup the SQLAlchemy DB Adapter
    UserManager(db_adapter, app)  # Init Flask-User and bind to app

    # Flask-Mail init
    mail.init_app(app)

    # Flask-Admin init
    admin.init_app(app)

    # Flask-Babel init
    babel.init_app(app)

    # Flask-Bcrypt init
    bcrypt.init_app(app)

    # Flask-Restful init
    from project.api import api
    api.init_app(app)

    # Blueprint registrations
    from project.main.views import homepage_blueprint
    app.register_blueprint(homepage_blueprint, url_prefix="/")

    from project.dashboard.views import dashboard_blueprint
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

    from project.tickets.views import tickets_blueprint
    app.register_blueprint(tickets_blueprint, url_prefix="/tickets")

    return app
