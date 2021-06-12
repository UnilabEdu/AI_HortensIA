from flask import Blueprint, render_template
from project import babel

@babel.localeselector
def get_locale():
    return 'en'

homepage_blueprint = Blueprint('homepage',
                               __name__,
                               template_folder='templates'
                               )


@homepage_blueprint.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
