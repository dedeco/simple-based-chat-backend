from flask import Flask
from flask_cors import CORS

from matchbox import database


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    CORS(app,
         supports_credentials=True,
         #resources={r"*": {"origins": app.config['INDEX_URL']}}
         resources={r"*": {"origins": "*"}}
         )
    database.db_initialization(app.config["FIREBASE_ADMIN_SDK_JSON"])


import src.chat
import src.health


def register_blueprints(app):
    app.register_blueprint(src.chat.chat_blueprint, url_prefix='/api/v1/chat')
    app.register_blueprint(src.health.health_blueprint, url_prefix='/api/v1/health')
