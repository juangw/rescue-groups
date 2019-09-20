from flask import render_template

import connexion
import os

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir="openapi/")
PORT = int(os.environ.get("PORT", 8080))
STAGE = os.environ.get("STAGE", "local")

from src.rescue_group.controllers.routes import *
from src.alpha_vantage.controllers.routes import *

def run():
    # app.add_api("my_api.yaml")
    app.run(debug=False, host="0.0.0.0", port=PORT)
