from flask_script import Command
from project.models import db
from project.models.user import UserModel, Role
from flask import current_app
from datetime import datetime


class InitDbCommand(Command):

    def run(self):
        init_db()


def init_db():
    db.drop_all()
    db.create_all()
    populate_db()


def populate_db():
    admin_role = find_or_create_role("Admin")

    find_or_create_user(username='username1',
                        password=current_app.user_manager.hash_password('password1'),
                        email='admin1@email.com',
                        role=admin_role)

    find_or_create_user(username='username2',
                        password=current_app.user_manager.hash_password('password2'),
                        email='user2@email.com')

    db.session.commit()


def find_or_create_role(name):
    role = Role.query.filter_by(name=name).first()

    if not role:
        role = Role(name)

        db.session.add(role)

    return role


def find_or_create_user(username, password, email, role=None):
    user = UserModel.query.filter_by(email=email).first()

    if not user:
        user = UserModel(username=username,
                    password=password,
                    email=email,
                    confirmed_at=datetime.utcnow(),
                    active=True)

        if role:
            user.roles.append(role)

        db.session.add(user)

    return user
