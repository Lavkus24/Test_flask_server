from flask import Blueprint

user_bp = Blueprint('user' , __name__)


@user_bp.route('/')
def users_home():
        return 'Hello from home user!'

@user_bp.route('/print')
def users_print_route():
    return 'Hi Lavksu, I am from the Noida'