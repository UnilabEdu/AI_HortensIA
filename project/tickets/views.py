from flask import Blueprint, render_template, request
# from project import babel, Config
from project.tickets.forms import EmotionForm
from project.models import Text, Ticket
from flask_user import current_user
import logging
from flask_user import login_required


tickets_blueprint = Blueprint('tickets',
                              __name__,
                              template_folder='templates'
                              )


@tickets_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def tickets():
    text = Text.get_random().text
    form = EmotionForm()

    if form.validate_on_submit():
        user = current_user.get_id()
        print(user)
        emotion = form.emotion.data
        print(emotion)
        ticket = Ticket(user, text, emotion)
        print(ticket)
        ticket.save_to_db()
        logging.basicConfig()
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

    return render_template('tickets.html', form=form, text=text)
