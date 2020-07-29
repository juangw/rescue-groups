from flask import Flask
from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient

from .db import init_db
from .config import GOOGLE_CLIENT_ID

login_manager = LoginManager()
# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)


def create_app():
    """Initialize the core application."""
    # Init flask app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "Testing"

    # Init db tables
    init_db()

    # User session management setup
    # https://flask-login.readthedocs.io/en/latest
    login_manager.init_app(app)

    with app.app_context():
        # Include our Routes
        from rescue_groups.controllers import auth  # noqa: E402, F403, F401
        from rescue_groups.controllers import routes  # noqa: E402, F403, F401

        return app
