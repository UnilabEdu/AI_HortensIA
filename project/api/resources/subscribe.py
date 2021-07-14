from flask_restful import Resource, reqparse
from project.models import SubscribedEmails


class Subscribe(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='missing email'
                        )

    def post(self):
        data = Subscribe.parser.parse_args()
        print('aaaaaaaaaaaaaaaaa')
        new_email = SubscribedEmails(data['email'])
        new_email.save_to_db()

        return {'success': 'email subscription successful'}, 200

        # return {'error': 'too many requests'}, 429