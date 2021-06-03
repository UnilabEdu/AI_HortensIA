from project.models import db
from flask_user import UserMixin


class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True, server_default='')
    confirmed_at = db.Column(db.DateTime())
    active = db.Column(db.Boolean(), nullable=False, server_default='1')
    tickets = db.relationship('Ticket', backref='users')
    roles = db.relationship('Role', secondary='user_roles')

    def __init__(self, username, password, email, confirmed_at, active):
        self.username = username
        self.password = password
        self.email = email
        self.confirmed_at = confirmed_at
        self.active = active



class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

    def __init__(self, user_id, role_id):
        self.user_id = user_id,
        self.role_id = role_id
