from src.rescue_group.models.parser import strip_tags
from common.utils.get_api_data import api_post_req
from flask import render_template

import connexion
import logging
import json
import os


LOG_LEVEL = getattr(logging, os.environ.get("LOG_LEVEL", "NOTSET"))

logging.basicConfig(level=LOG_LEVEL)
log = logging.getLogger("api_projects")
log.addHandler(logging.StreamHandler())
log.setLevel(LOG_LEVEL)

log.debug("Start of Program, Testing Debugger")

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='openapi/')


@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:8090/

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
            "operation": "greaterthan",
            "criteria": "48103"
        },
        {
            "fieldName": "animalLocation",
            "operation": "lessthan",
            "criteria": "48198"
        },
        {
            "fieldName": "animalLocation",
            "operation": "lessthan",
            "criteria": "48198"
        },
    ]
    default_fields = [
        "animalID",
        "animalOrgID",
        "locationPhone",
        "fosterPhoneCell",
        "fosterEmail",
        "animalName",
        "animalDescription",
        "animalThumbnailUrl",
        "animalPictures",
        "animalSex",
        "animalAdoptionFee",
        "animalBreed",
        "animalColor",
        "animalEyeColor",
        "animalAgeString",
        "animalGeneralAge",
        "animalBirthdate",
        "animalLocationCitystate",
        "animalLocationState",
        "animalLocation",
        "locationAddress",
        "locationUrl",
        "animalAffectionate",
        "animalApartment",
        "animalIntelligent",
        "animalLap",
        "animalActivityLevel"
    ]
    log.debug("Attempting to gather API data")
    results = api_post_req("rescue_group", default_filter, default_fields)
    if results is not None:
        result_dict = json.loads(results)
        return render_template(
            "home.html", results=result_dict, strip_tags=strip_tags
        )
    else:
        return render_template("error.html")


def run():
    # app.add_api('my_api.yaml')
    app.run(debug=True, host="0.0.0.0", port=8080)
