from src.rescue_group.utils.call_rescue_group import api_post_req
from src.rescue_group.models.parser import strip_tags
from flask import render_template, request, redirect, url_for
from api_projects.log import log

import connexion
import json

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='openapi/')


@app.route("/animals")
def animals_home(page=1):
    """
    This function just responds to the browser URL
    localhost:8090/

    :return:        the rendered template "home.html"
    """
    error = ""
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
    start = (int(page) - 1) * 20
    stop = int(page) * 20
    results = api_post_req(
        "rescue_group", start, stop, default_filter, default_fields
    )
    if results is not None:
        result_dict = json.loads(results)
        if not result_dict.get("data", {}):
            error = "There were no results for your search"
            return render_template("error.html", error=error)
        return render_template(
            "animals.html",
            results=result_dict,
            page=page,
            limits=[start, stop],
        )
    else:
        return render_template("error.html", error=error)


@app.route("/animals/<page>")
def animals(page=None):
    """
    This function just responds to the browser URL
    localhost:8090/

    :return:        the rendered template "home.html"
    """
    error = ""
    if page is None:
        page = 1
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
    start = (int(page) - 1) * 20
    stop = int(page) * 20
    results = api_post_req(
        "rescue_group", start, stop, default_filter, default_fields
    )
    if results is not None:
        result_dict = json.loads(results)
        if not result_dict.get("data", {}):
            error = "There were no results for your search"
            return render_template("error.html", error=error)
        return render_template(
            "animals.html",
            results=result_dict,
            page=page,
            limits=[start, stop],
        )
    else:
        return render_template("error.html", error=error)


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
            "animalPictures",
            "animalSex",
            "animalAdoptionFee",
            "animalColor",
            "animalEyeColor",
            "animalAgeString",
            "animalGeneralAge",
            "animalLocationCitystate",
            "locationAddress",
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
            "animal.html",
            results=result_dict,
            animal_id=animal_id,
            strip_tags=strip_tags,
        )
    else:
        return render_template("error.html")


def run():
    # app.add_api('my_api.yaml')
    app.run(debug=True, host="0.0.0.0", port=8080)
