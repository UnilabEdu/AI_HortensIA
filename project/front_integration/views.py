from flask import Blueprint, render_template, request, session, current_app
from project import babel, Config
from project.models import SubscribedEmails


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(Config.LANGUAGES.keys())
    # return "en"


homepage_blueprint = Blueprint('homepage',
                               __name__,
                               template_folder='templates'
                               )


@homepage_blueprint.route('/', methods=['GET', 'POST'])
def index():
    user_manager = current_app.user_manager

    login_form = user_manager.login_form(request.form)          # for login.html
    register_form = user_manager.register_form()                # for login_or_register.html

    # if subscribe_form.validate_on_submit():
    #     session['subscribe_email'] = subscribe_form.email
    #     print(session['subscribe_email'])
    # else:
    #     print('invalid email')

    return render_template('index.html',
                           form=login_form,
                           login_form=login_form,
                           register_form=register_form)


# @homepage_blueprint.route('/subscribe', methods=['GET', 'POST'])
# def subscribe():
#     print(request.json)
#     email = 1
#     return {'done': 'done'}
