from .api_routes import api_bp
from .admin_routes import admin_api
from .user_routes import user_bp

    
def register_routes(app):
    app.register_blueprint(admin_api, url_prefix='/admin')
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(user_bp, url_prefix='/users')
