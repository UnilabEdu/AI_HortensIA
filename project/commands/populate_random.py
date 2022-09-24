from datetime import datetime, timedelta, date
from random import randrange, choice

from essential_generators import DocumentGenerator
from flask import current_app

from project.models import db, Ticket, ActivityStreak
from project.models.user import User
from .populate_initial import populate_emotions, populate_texts, populate_files

gen = DocumentGenerator()  # used to generate random words and sentences



def populate_with_random():
    populate_users()
    populate_emotions()
    populate_files()
    db.session.commit()

    populate_texts()
    populate_tickets()
    populate_streaks()
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


def populate_tickets():
    emotion_id_list = range(1, 34)  # IDs of all emotions

    date_end = datetime.now()  # max date
    date_max_difference = 90  # max difference (in days) between today and Ticket submission date

    # Iterate over 300 User IDs
    for user_id in range(1, 301):
        text_id_list = list(range(1, 2736))

        # Random numbers used to skip some dates to better showcase Streaks
        skip_these_dates = [date_end - timedelta(days=randrange(1, 90)) for i in range(1, randrange(1, 10))]

        filled_tickets = randrange(0, 600)  # amount of tickets for current user

        for i in range(filled_tickets):
            text_id = choice(text_id_list)  # choose a random text to assign to current ticket
            text_id_list.remove(text_id)  # remove the used ticket from the next iteration for current user
            emotion_id = choice(emotion_id_list)  # choose a random emotion to assign to current ticket
            date = date_end - timedelta(days=randrange(0, date_max_difference))  # choose a random date for the ticket

            if date in skip_these_dates:
                # some dates are skipped to make the activity data more varying
                continue

            ticket = Ticket(user_id=user_id,
                            text_id=text_id,
                            emotion_id=emotion_id,
                            commit_date=date)

            db.session.add(ticket)


def populate_streaks():
    for i in range(100):
        start_date = date.today() - timedelta(days=randrange(1, 100))
        total_days = randrange(1, 100)
        end_date = start_date + timedelta(days=total_days)

        db.session.add(ActivityStreak(
                            user_id=randrange(1, 301),
                            start_date=start_date,
                            end_date=end_date,
                            total_days=total_days,
                            status=1
                            )
                       )

    db.session.commit()
