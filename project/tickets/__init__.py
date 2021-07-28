from flask import Blueprint

tickets_blueprint = Blueprint('tickets',
                              __name__,
                              template_folder='templates',
                              static_folder='static'
                              )