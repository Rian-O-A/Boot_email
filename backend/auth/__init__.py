from flask import Flask
from backend.auth.route import auth_route

app = Flask(__name__)

def create_app():
    
    app.register_blueprint(auth_route, url_prefix='')
    
    return app

