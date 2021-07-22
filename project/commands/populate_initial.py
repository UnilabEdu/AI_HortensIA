from flask_script import Command
from project.models import db, Emotion, Text
from project.models.user import User, Role
from flask import current_app
from datetime import datetime
from random import randrange
from essential_generators import DocumentGenerator


gen = DocumentGenerator()


class PopulateInitial(Command):

    def run(self):
        populate_initial()


def populate_initial():
    db.drop_all()
    db.create_all()
    populate_db()


def populate_db():
    admin_role = find_or_create_role("Admin")

    find_or_create_user(username='admin',
                        password=current_app.user_manager.hash_password('password'),
                        email='admin@email.com',
                        role=admin_role)

    find_or_create_user(username='user',
                        password=current_app.user_manager.hash_password('password'),
                        email='user@email.com')

    populate_emotions()
    populate_texts()

    db.session.commit()


def find_or_create_role(name):
    role = Role.query.filter_by(name=name).first()

    if not role:
        role = Role(name)

        db.session.add(role)

    return role


def find_or_create_user(username, password, email, role=None):
    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(username=username,
                    password=password,
                    email=email,
                    confirmed_at=datetime.utcnow(),
                    active=True)

        if role:
            user.roles.append(role)

        db.session.add(user)

    return user


def populate_emotions():
    emotions_list_en = [  # Primary Emotions
        "Rage", "Anger", "Annoyance",
        "Vigilance", "Anticipation", "Interest",
        "Ecstasy", "Joy", "Serenity",
        "Admiration", "Trust", "Acceptance",
        "Terror", "Fear", "Apprehension",
        "Amazement", "Surprise", "Distraction",
        "Grief", "Sadness", "Pensiveness",
        "Loathing", "Disgust", "Boredom",
        # Secondary Emotions
        'Aggressiveness', 'Optimism', 'Love', 'Submission', 'Awe', 'Disapproval', 'Remorse', 'Contempt', 'Neutral'
    ]

    emotions_list_ka = [  # ძირითადი ემოციები TODO: improve translations
        'რისხვა', 'ბრაზი', 'გაღიზიანება',
        'სიფხიზლე', 'მოლოდინი', 'ინტერესი',
        'აღტყინება', 'სიხარული', 'სიმშვიდე',
        'აღტაცება', 'ნდობა', 'მიმღებლობა',
        'თავზარდამცემი შიში', 'შიში', 'ღელვა',
        'აღფრთოვანება', 'გაკვირვება', 'ყურადღების გაფანტვა',
        'მწუხარება', 'სევდა', 'ნაღვლიანობა',
        'სიძულვილი', 'გულისრევა', 'მოწყენილობა',
        # დამატებითი ემოციები
        'აგრესია', 'ოპტიმიზმი', 'სიყვარული', 'მორჩილება', 'განცვიფრება', 'გაკიცხვა', 'სინანული', 'ზიზღი', 'ნეიტრალური'
    ]

    examples_en = ['I feel ' + emotion for emotion in emotions_list_en]
    examples_ka = [emotion + ' ემოციაა' for emotion in emotions_list_ka]

    for emotion_en, example_en, emotion_ka, example_ka in zip(emotions_list_en, examples_en, emotions_list_ka, examples_ka):
        db.session.add(Emotion(name_en=emotion_en,
                               synonym_en=emotion_en,
                               example_en=example_en,
                               name_ka=emotion_ka,
                               synonym_ka=emotion_ka,
                               example_ka=example_ka))


def populate_texts():
    for i in range(4000):
        db.session.add(Text(text=gen.sentence(), file=randrange(1, 6)))