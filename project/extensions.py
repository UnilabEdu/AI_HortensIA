from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_restful import Api


db = SQLAlchemy()
migrate = Migrate(render_as_batch=True)
babel = Babel()
mail = Mail()
bcrypt = Bcrypt()
login_manager = LoginManager()
api = Api(prefix='/api/')

extensions_list = [db, babel, mail, bcrypt, login_manager, api]
extensions_db_list = [migrate]
