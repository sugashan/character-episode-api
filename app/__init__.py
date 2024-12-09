import os
import logging
from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from dotenv import load_dotenv

from app.routes.v1 import auth, characters, favorites
from app.db.mongo_manager import init_db


load_dotenv(dotenv_path='.env')

logging.basicConfig(level=logging.INFO)


class APIConfig:
    API_TITLE = "Character Cards API"
    API_VERSION = "v1.0"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret_key')
    # SESSION_COOKIE_SAMESITE = 'None'
    # SESSION_COOKIE_HTTPONLY = True
    # SESSION_COOKIE_SECURE = False


def create_app():
    
    server = Flask(__name__)

    server.config.from_object(APIConfig)

    server.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback_secret_key')
    server.config['SESSION_COOKIE_NAME'] = 'session'
    server.config['SESSION_COOKIE_HTTPONLY'] = True
    server.config['SESSION_COOKIE_SECURE'] = False
    server.config['SESSION_COOKIE_SAMESITE'] = 'None'

    CORS(server, supports_credentials=True)

    api = Api(server)

    api.register_blueprint(auth, url_prefix='/api/v1/auth')
    api.register_blueprint(characters, url_prefix='/api/v1')
    api.register_blueprint(favorites, url_prefix='/api/v1')

    init_db()

    print(server.config['SECRET_KEY'])

    return server
