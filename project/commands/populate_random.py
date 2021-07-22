from flask_script import Command
from project.models import db, Ticket, Text, Files
from project.models.user import User
from essential_generators import DocumentGenerator
from random import randrange, choice
from flask import current_app
from datetime import datetime, timedelta
from .populate_initial import populate_emotions, populate_texts

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
    populate_files()
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

    active = 1
    confirmed_at = datetime.now()

    for username, email in zip(usernames, emails):
        db.session.add(User(username=username,
                            password=hashed_password,
                            email=email,
                            active=active,
                            confirmed_at=confirmed_at))


def populate_files():
    for i in range(5):
        random_word = gen.word() + gen.word()
        random_number = str(randrange(1, 2000))
        db.session.add(Files(title=random_word+' '+random_number,
                             file_name=random_word+'_'+random_number,
                             user_id=randrange(1, 301)))





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
                            commit_date=date)

            db.session.add(ticket)
