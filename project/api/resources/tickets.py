import pandas as pd
from flask import jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_restful import Resource, reqparse
from flask_user import current_user
from sqlalchemy.orm import load_only
from sqlalchemy.sql.expression import func

from project import create_app
from project.database import db
from project.models import Text, Ticket, ActivityStreak


class GetTextPostTicket(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text',
                        type=int,
                        required=True,
                        help='missing text ID'
                        ),
    parser.add_argument('emotion',
                        type=int,
                        required=True,
                        help='missing emotion ID'
                        ),
    parser.add_argument('user',
                        type=int,
                        required=True,
                        help='missing user ID'
                        ),
    parser.add_argument('secret',
                        type=str,
                        required=True,
                        help='missing secret'
                        )

    def get(self):
        """
        returns a dictionary with data which should be used to submit a ticket. the keys are: user, secret, text
        :user: ID of current_user (currently logged-in user which will be the author of the submitted ticket)
        :secret: generates a hash of the app's SECRET_KEY which is required to submit a ticket
        :text: a dictionary containing attributes of a Text object as its keys (id (int), text (str), file (int))
        """

        with create_app().app_context():
            if current_user.__class__.__name__ == 'AnonymousUserMixin':  # when sending requests outside browsers
                return {'error', 'You are not logged in. Please use the website to log in and submit tickets'}, 403

            marked_texts = pd.read_sql(  # get IDs of texts that the used has already marked (submitted a ticket)
                Ticket.query.filter_by(user=current_user.id).options(
                    load_only('text')).statement, db.engine)

            marked_texts = marked_texts.text.to_list()

            # get texts not yet marked by user, based on marked texts
            unmarked_texts = db.session.query(Text).filter(Text.id.notin_(marked_texts))
            random_text = unmarked_texts.order_by(func.random()).first()  # get a random text out of on unmarked texts

            if random_text.text:  # if there is an unmarked text left
                secret = generate_password_hash(create_app().config['SECRET_KEY'])  # hash the SECRET_KEY

                # create a response dictionary and add text, user and secret keys
                response = dict(random_text.__dict__)  # convert the randomly selected Text object to type dict
                response.pop('_sa_instance_state')  # remove an unnecessary key from the Text dictionary
                # add user id to response dictionary and secret key converted to JSON
                response.update(user=current_user.id, secret=secret.decode('utf8').replace("'", '"'))
                return jsonify(response)

            else:  # if there are no unmarked texts, return False so the ticket view notifies the user accordingly
                return False

    def post(self):
        """
        adds a ticket to db based on current_user ID, received text ID and
        """

        if current_user.__class__.__name__ == 'AnonymousUserMixin':  # when sending requests outside browsers
            return {'error', 'You are not logged in. Please use the website to log in and submit tickets'}, 403

        data = GetTextPostTicket.parser.parse_args()
        if check_password_hash(data['secret'], create_app().config['SECRET_KEY']) and current_user.id == data['user']:
            net_ticket = Ticket(current_user.id, data['text'], data['emotion'] + 1)
            net_ticket.save_to_db()

            # create or update streak
            current_streak = ActivityStreak.query.filter_by(user=current_user.id, status=1).first()

            if current_streak and current_streak.update_streak():
                pass  # update_streak updates an active streak upon being called
            else:
                new_streak = ActivityStreak(current_user.id)
                db.session.add(new_streak)
                db.session.commit()

            return {'success': 'ticket added'}, 200

        else:  # if the secret is wrong (user didn't use the website to submit the ticket)
            return {'error': 'Secret_key is wrong. Use the website to send requests'}, 400
