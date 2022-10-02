from flask import render_template
from flask_user import login_required
from flask import Blueprint

tickets_blueprint = Blueprint('tickets',
                              __name__,
                              template_folder='templates',
                              static_folder='static'
                              )



@tickets_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def tickets():
    """
    renders a text which can be marked with an emotion chosen with the emotion-wheel selector
    texts and emotions are fetched with JavaScript with the API and submitted in the same way
    """

    return render_template('tickets/tickets.html')
