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
        """
        adds a received email address to 'subscribed_emails' column in db
        """

        data = Subscribe.parser.parse_args()
        new_email = SubscribedEmails(data['email'])
        new_email.save_to_db()

        return {'success': 'email subscription successful'}, 200
