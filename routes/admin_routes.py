from flask import Blueprint
from datetime import datetime, timedelta
from opensearchpy import OpenSearch
# Create a Blueprint instance
from flask import jsonify
admin_api = Blueprint('admin', __name__)

@admin_api.route('/')
def admin_home():
    return 'Hello from home admin!'
