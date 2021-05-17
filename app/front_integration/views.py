from flask import render_template, Blueprint

homepage_blueprint = Blueprint('front_integration',
                               __name__,
                               template_folder='templates')


@homepage_blueprint.route('/', methods=['GET'])
def homepage():
    return render_template("base.html")
