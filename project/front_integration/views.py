from flask import render_template, Blueprint
from flask_login import current_user

homepage_blueprint = Blueprint('front_integration',
                               __name__,
                               template_folder='templates')


@homepage_blueprint.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template("base.html", current_user=current_user)

