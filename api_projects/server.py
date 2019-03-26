from common.utils.get_api_data import api_post_req
from flask import render_template

import connexion
import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

logger.debug("Start of Program, Testing Debugger")

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='openapi/')


@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    default_filter = [
        {
            "fieldName": "animalSpecies",
            "operation": "equals",
            "criteria": "cat"
        },
        {
            "fieldName": "animalLocation",
            "operation": "equals",
            "criteria": "48105"
        }
    ]
    default_fields = [
        "animalID",
        "animalOrgID",
        "locationPhone",
        "animalName",
        "animalThumbnailUrl",
        "animalPictures",
        "animalSex",
        "animalAdoptionFee",
        "animalBreed",
        "animalColor",
        "animalEyeColor",
        "animalAgeString",
        "animalLocation",
        "animalAffectionate",
        "animalApartment",
        "animalIntelligent",
        "animalLap",
        "animalActivityLevel"
    ]

    text = api_post_req("rescue_group", default_filter, default_fields)
    print(text)
    return render_template("home.html")


def run():
    app.add_api('my_api.yaml')
    app.run(debug=True, port=8080)
