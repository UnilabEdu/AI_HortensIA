from flask import Blueprint, render_template, request, session
from project import babel, Config
from project.subscribe_function.subscribe_form import subscribe_form
from project.tickets.forms import EmotionForm
from project.models import Text, Ticket
from flask_user import current_user


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(Config.LANGUAGES.keys())
    # return "en"


homepage_blueprint = Blueprint('homepage',
                               __name__,
                               template_folder='templates'
                               )


@homepage_blueprint.route('/', methods=['GET', 'POST'])
def home():
    email = None
    form = subscribe_form()

    if form.validate_on_submit():
        session['email'] = email
        print(session['email'])

    # თეგირების ფანჯარა
    text = Text.get_random().text
    ticket_form = EmotionForm()

    if ticket_form.validate_on_submit():
        user = current_user.get_id()
        print(user)
        emotion = ticket_form.emotion.data
        ticket = Ticket(user, text, emotion)
        print(ticket)
        ticket.save_to_db()

    return render_template('home.html', form=form, email=email, ticket_form=ticket_form, text=text)
