from flask import Flask
from app.routes import main
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()  
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    app.register_blueprint(main)

    return app
