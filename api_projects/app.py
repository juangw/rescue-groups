from src.rescue_group.utils.call_rescue_group import api_post_req
from src.rescue_group.models.parser import strip_tags
from flask import render_template, request, redirect, url_for
from api_projects.log import log

import connexion
import json

start = 0
stop = 20

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='openapi/')


@app.route("/animals", methods=["GET", "POST"])
def home(start=start, stop=stop):
    """
    This function just responds to the browser URL
    localhost:8090/

    :return:        the rendered template "home.html"
    """
    if request.method == "POST":
        start += 20
        stop += 20
        return redirect(url_for("home", start=start, stop=stop))
    else:
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
                "criteria": "48109"
            },
        ]
        default_fields = [
            "animalName",
            "animalThumbnailUrl",
            "animalSex",
            "animalGeneralAge",
            "animalLocationCitystate",
            "locationAddress",
        ]
        log.debug("Attempting to gather API data")
        results = api_post_req(
            "rescue_group", start, stop, default_filter, default_fields
        )
        if results is not None:
            result_dict = json.loads(results)
            return render_template(
                "animals.html",
                results=result_dict,
                limits=[start, stop],
            )
        else:
            return render_template("error.html")


@app.route("/animal/<animal_id>")
def animal(animal_id):
    """
    This function just responds to the browser URL
    localhost:8090/

    :return:        the rendered template "home.html"
    """
    animal_filter = [
        {
            "fieldName": "animalID",
            "operation": "equals",
            "criteria": animal_id
        }
    ]
    default_fields = [
            "animalName",
            "animalDescription",
            "animalThumbnailUrl",
            "animalPictures",
            "animalSex",
            "animalAdoptionFee",
            "animalColor",
            "animalEyeColor",
            "animalAgeString",
            "animalGeneralAge",
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
    results = api_post_req(
        "rescue_group", 0, 1, animal_filter, default_fields
    )
    if results is not None:
        result_dict = json.loads(results)
        return render_template(
            "animal.html", results=result_dict, strip_tags=strip_tags
        )
    else:
        return render_template("error.html")


def run():
    # app.add_api('my_api.yaml')
    app.run(debug=True, host="0.0.0.0", port=8080)
