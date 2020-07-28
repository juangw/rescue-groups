from flask import Flask  # noqa E402

import logging  # noqa E402


def create_app():
    """Initialize the core application."""
    # Init flask app
    app = Flask(__name__)

    with app.app_context():
        # Include our Routes
        from rescue_groups.controllers import routes  # noqa: E402, F403, F401

        return app