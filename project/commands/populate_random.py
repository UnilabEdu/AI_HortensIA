from flask_script import Command
from project.models import db, Emotion, Ticket, Text
from project.models.user import UserModel
from essential_generators import DocumentGenerator
from random import randrange, choice
from flask import current_app
from datetime import datetime, timedelta


gen = DocumentGenerator()  # used to generate random words and sentences


class PopulateWithRandomCommand(Command):
    """
    Populates DB with Users and Texts with randomized data, Emotions,
    and Tickets related to those Users, Texts and Emotions
    """

    def run(self):
        db.drop_all()  # uncomment next two lines if db_init wasn't used and DB wasn't populated yet
        db.create_all()
        populate_with_random()


def populate_with_random():
    populate_users()
    populate_texts()
    populate_emotions()
    populate_tickets()

    db.session.commit()


def populate_users():
    #  Generate a hashed password
    user_manager = current_app.user_manager
    hashed_password = user_manager.hash_password('password')

    users_amount = 300  # amount of users to generate

    usernames = ['User_' + gen.word().capitalize() + str(randrange(1, 2003)) for i in range(users_amount)]
    emails = [gen.word()[:3] + gen.email() for i in range(users_amount)]

    confirmed_at = datetime.now()
    active = 1

    for username, email in zip(usernames, emails):
        db.session.add(UserModel(username=username,
                                 password=hashed_password,
                                 email=email,
                                 confirmed_at=confirmed_at,
                                 active=active))


def populate_texts():
    for i in range(4000):
        db.session.add(Text(text=gen.sentence()))


def populate_emotions():
    emotions_list = [  # Primary Emotions
        "Rage", "Anger", "Annoyance",
        "Vigilance", "Anticipation", "Interest",
        "Ecstasy", "Joy", "Serenity",
        "Admiration", "Trust", "Acceptance",
        "Terror", "Fear", "Apprehension",
        "Amazement", "Surprise", "Distraction",
        "Grief", "Sadness", "Pensiveness",
        "Loathing", "Disgust", "Boredom",
        # Secondary Emotions
        'Aggressiveness', 'Optimism', 'Love', 'Submission', 'Awe', 'Disapproval', 'Remorse', 'Contempt'
    ]
    examples = ['I feel ' + emotion for emotion in emotions_list]

    for emotion, example in zip(emotions_list, examples):
        db.session.add(Emotion(name=emotion,
                               synonym=emotion,
                               example=example))


def populate_tickets():
    emotion_id_list = range(1, 33)  # IDs of all emotions

    date_end = datetime.now()  # max date
    date_max_difference = 90  # max difference (in days) between today and Ticket submission date

    # Iterate over 30 User IDs
    for user_id in range(1, 301):
        text_id_list = list(range(1, 4001))

        # Random numbers used to skip some dates to better showcase Streaks
        skip_these_dates = [date_end - timedelta(days=randrange(1, 90)) for i in range(1, randrange(1, 10))]

        filled_tickets = randrange(2800, 4000)  # amount of tickets for current user

        for i in range(filled_tickets):
            text_id = choice(text_id_list)  # choose a random text to assign to current ticket
            text_id_list.remove(text_id)  # remove the used ticket from the next iteration for current user
            emotion_id = choice(emotion_id_list)  # choose a random emotion to assign to current ticket
            date = date_end - timedelta(days=randrange(0, date_max_difference))

            if date in skip_these_dates:
                continue

            ticket = Ticket(user_id=user_id,
                            text_id=text_id,
                            emotion_id=emotion_id,
                            date=date)

            db.session.add(ticket)
