from flask import Blueprint

homepage_blueprint = Blueprint('homepage',
                               __name__,
                               template_folder='templates'
                               )
