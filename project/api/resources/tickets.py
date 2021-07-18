from flask_restful import Resource, reqparse
from project import create_app
from project.database import db
from project.models import Text, Ticket
from flask_user import current_user
from sqlalchemy.orm import load_only
import pandas as pd
from sqlalchemy.sql.expression import func
from flask import jsonify, session
from flask_bcrypt import generate_password_hash, check_password_hash


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
        with create_app().app_context():

            marked_texts = pd.read_sql(Ticket.query.filter_by(user=current_user.id).options(load_only('text')).statement, db.engine)
            marked_texts = marked_texts.text.to_list()

            unmarked_texts = db.session.query(Text).filter(Text.id.notin_(marked_texts))
            random_text = unmarked_texts.order_by(func.random()).first()

            if random_text.text:
                secret = generate_password_hash(create_app().config['SECRET_KEY'])

                response = dict(random_text.__dict__)
                response.pop('_sa_instance_state')
                response.update(user=current_user.id, secret=secret.decode('utf8').replace("'", '"'))
                print(response)

                return jsonify(response)
            else:
                return False


    def post(self):
        print('Received Ticket POST request')
        data = GetTextPostTicket.parser.parse_args()
        print(data)
        if check_password_hash(data['secret'], create_app().config['SECRET_KEY']):
            print('secret check successful')
            net_ticket = Ticket(data['user'], data['text'], data['emotion']+1)
            net_ticket.save_to_db()
            print('final success')
            return {'success': 'ticket added'}, 200
        else:
            return {'error': 'secret key is wrong. use the website to send requests'}, 400
