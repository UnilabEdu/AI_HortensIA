import datetime
from flask_user import UserManager
from project.database import db
from project.models.user import UserModel


class Profile(db.Model):
    __tablename__ = "profiles"

    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    profile_img_url = db.Column(db.String)
    # gender - gasarkvevia
    # date_of_birth - gasarkvevia

    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name


class Emotion(db.Model):
    __tablename__ = "emotions"
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    synonym = db.Column(db.String(80), nullable=False)
    example = db.Column(db.Text)
    tickets = db.relationship('Ticket', backref='emotion')

    def __init__(self, name, synonyms, description):
        self.name = name
        self.synonym = synonyms
        self.example = description

    def __repr__(self):
        return self.name


class Text(db.Model):
    __tablename__ = "texts"
    id = db.Column(db.String, primary_key=True)
    text = db.Column(db.Text)
    tickets = db.relationship('Ticket', backref='text')

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return self.text


class Ticket(db.Model):
    __tablename__ = "tickets"
    id = db.Column(db.String, primary_key=True)
    user = db.Column(db.String, db.ForeignKey('users.id'))
    text = db.Column(db.Text, db.ForeignKey('texts.id'))
    emotion = db.Column(db.String, db.ForeignKey('emotions.id'))
    date = db.Column(db.DateTime)

    def __repr__(self):
        return f'{self.user} - {self.text}'

