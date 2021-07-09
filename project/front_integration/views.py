from flask import Blueprint, render_template, request, session
from project import babel, Config
from project.subscribe_function.subscribe_form import subscribe_form


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

    return render_template('home.html', form=form, email=email)
