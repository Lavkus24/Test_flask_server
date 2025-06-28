from flask import Blueprint

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def home():
        return 'Hello from home route!'

@api_bp.route('/print')
def print_route():
        return 'I am from the Noida'
