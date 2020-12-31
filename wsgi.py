#!/usr/bin/env python3
from rescue_groups import create_app
from rescue_groups.db import session

import flask
import os

PORT = int(os.environ.get("PORT", 8080))
# This allows us to use a plain HTTP callback
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = create_app()

@app.before_request
def create_session():
    flask.g.session = session

@app.teardown_appcontext
def shutdown_session(response_or_exc):
    flask.g.session.remove()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, ssl_context="adhoc")
