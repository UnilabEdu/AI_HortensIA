from flask import Blueprint, render_template, request, session, current_app, redirect, url_for, jsonify, make_response
from project import babel, Config
from project.models import SubscribedEmails
# from flask_babel import get_locale


homepage_blueprint = Blueprint('homepage',
                               __name__,
                               template_folder='templates'
                               )


@babel.localeselector
def get_locale():
    if 'locale' not in session.keys():
        session['locale'] = 'ka'
    return session['locale']


# @homepage_blueprint.route('/currentlang', methods=['GET', 'POST'])
# def current_lang():
#     if 'locale' not in session.keys():
#         return make_response(jsonify(
#             dict(language='ka')
#         ))
#
#     else:
#         return make_response(jsonify(
#             dict(language=session['locale'])
#         ))


@homepage_blueprint.route('/language', methods=['GET', 'POST'])
def toggle_lang():
    if 'locale' in session.keys():
        if session['locale'] == 'en':
            session['locale'] = 'ka'
        elif session['locale'] == 'ka':
            session['locale'] = 'en'
    else:
        session['locale'] = 'ka'

    if request.referrer:
        return redirect(request.referrer)
    else:
        return redirect(url_for('user.login'))


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
