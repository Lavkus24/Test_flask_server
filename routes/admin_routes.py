from flask import Blueprint

# Create a Blueprint instance
admin_api = Blueprint('admin', __name__)

@admin_api.route('/')
def admin_home():
    return 'Hello from home admin!'

@admin_api.route('/print')
def admin_print_route():
    return 'Hi Admin, I am from Noida'
