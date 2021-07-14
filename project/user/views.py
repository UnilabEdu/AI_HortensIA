from flask import Blueprint, render_template


user_blueprint = Blueprint('User',
                           __name__,
                           template_folder='templates/user'
                           )


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@user_blueprint.route('/registration', methods=['GET', 'POST'])
def registration():
    return render_template('register.html')
