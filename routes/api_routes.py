from flask import Blueprint
from opensearchpy import OpenSearch, NotFoundError

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def home():
    try:
        return "I am from api"

    except Exception as e:
        return {"error": str(e)}, 500


@api_bp.route('/print')
def print_route():
        return 'I am from the Noida'
