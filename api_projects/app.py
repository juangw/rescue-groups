import connexion
import os

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir="openapi/")
PORT = int(os.environ.get("PORT", 8080))

from src.rescue_group.routes import home

def run():
    # app.add_api("my_api.yaml")
    app.run(debug=True, host="0.0.0.0", port=PORT)