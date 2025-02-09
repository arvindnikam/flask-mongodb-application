from flask import Flask
from flask_cors import CORS

from app.db import init_db
from app.exceptions import configure_exception_handler
from app.config import configure_app, configure_celery
from app.routes import initialize_routes

def create_app(test_config=None):
    # Configure the logger

    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    configure_app(app)
    celery = configure_celery(app)
    init_db(app)
    CORS(app)
    configure_exception_handler(app)
    initialize_routes(app)

    # Autocomplete in flask shell
    import rlcompleter, readline
    readline.parse_and_bind('tab:complete')

    return app
