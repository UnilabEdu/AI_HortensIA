from flask import request, session, redirect, url_for

from project.extensions import babel
from . import homepage_blueprint


# the index page uses Flask-User login_or_register endpoint backend

@babel.localeselector
def get_locale():
    """
    returns current language and stores it in session['locale']
    the default language is 'ka'
    """
    if 'locale' not in session.keys():
        session['locale'] = 'ka'
    return session['locale']


@homepage_blueprint.route('/language', methods=['GET', 'POST'])
def toggle_lang():
    """
    toggles language: from 'ka' to 'en' or from 'en' to 'ka' and changes it in session['locale']
    """
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
