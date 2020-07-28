import connexion
import os

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir="openapi/")
PORT = int(os.environ.get("PORT", 8080))
STAGE = os.environ.get("STAGE", "local")

from rescue_groups.controllers.routes import *  # noqa: E402, F403, F401


def run():
    # app.add_api("my_api.yaml")
    app.run(debug=False, host="0.0.0.0", port=PORT)
