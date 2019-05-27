from src.rescue_group.utils.call_rescue_group import api_post_req
from src.rescue_group.models.parser import strip_tags
from src.rescue_group.utils.all_fields import ALL_FIELDS
from src.rescue_group.utils.db_query import (
    save_animal, remove_animal, list_saved_animals
)
from flask import render_template, request
from api_projects.log import log

import connexion
import json
import os

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir="openapi/")
PORT = int(os.environ.get("PORT", 8080))
default_fields = [
    "animalName",
    "animalThumbnailUrl",
    "animalSex",
    "animalGeneralAge",
    "locationPostalcode",
    "locationAddress",
]


@app.route("/")
@app.route("/animals")
@app.route("/animals/")
def home(page=1):
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
            "fieldName": "locationPostalcode",
            "operation": "equals",
            "criteria": "48105"
        },
    ]
    log.debug("Attempting to gather API data")
    start = (int(page) - 1) * 20
    results = api_post_req(
        "rescue_group", start, default_filter, default_fields
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
            save_animal=save_animal,
            limits=[start, start+20],
        )
    else:
        return render_template("error.html", error=error)


@app.route("/saved-animals")
def animals_saved():
    """
    This function just responds to the browser URL
    localhost:8090/

    :return:        the rendered template "home.html"
    """
    try:
        saved_animals = list_saved_animals()
        return render_template(
            "saved.html",
            results=saved_animals,
            count=len(saved_animals),
        )
    except Exception as e:
        return render_template("error.html", error=e)


@app.route("/animals/<page>", methods=["GET", "POST"])
@app.route("/animals/<page>/age-<age>", methods=["GET", "POST"])
@app.route("/animals/<page>/gender-<gender>", methods=["GET", "POST"])
@app.route("/animals/<page>/loc-<location>", methods=["GET", "POST"])
@app.route(
    "/animals/<page>/age-<age>/gender-<gender>", methods=["GET", "POST"]
)
@app.route("/animals/<page>/age-<age>/loc-<location>", methods=["GET", "POST"])
@app.route(
    "/animals/<page>/gender-<gender>/loc-<location>", methods=["GET", "POST"]
)
@app.route(
    "/animals/<page>/age-<age>/gender-<gender>/loc-<location>",
    methods=["GET", "POST"],
)
def animals_page_filter(page=None, age=None, gender=None, location=None):
    """
    This function just responds to the browser URL
    localhost:8090/

    :return:        the rendered template "home.html"
    """
    if gender is None:
        gender = request.form.get("gender", None)
    if location is None:
        location = request.form.get("location", None)
    if age is None:
        age = request.form.get("age", None)
    error = ""
    default_filter = [
        {
            "fieldName": "animalSpecies",
            "operation": "equals",
            "criteria": "cat"
        },
    ]
    if page is None:
        page = 1
    if age not in [None, "None"]:
        age_filter = {
            "fieldName": "animalGeneralAge",
            "operation": "equals",
            "criteria": age
        }
        default_filter.append(age_filter)
    if gender not in [None, "None"]:
        gender_filter = {
            "fieldName": "animalSex",
            "operation": "equals",
            "criteria": gender
        }
        default_filter.append(gender_filter)
    if location not in ["", None, "None"]:
        location_filter = {
            "fieldName": "locationPostalcode",
            "operation": "equals",
            "criteria": location
        }
        default_filter.append(location_filter)
    else:
        location_filter = {
            "fieldName": "locationPostalcode",
            "operation": "equals",
            "criteria": "48105"
        }
        default_filter.append(location_filter)
    log.info(f"FILTER: {default_filter}\nPAGE: {page}")
    log.debug("Attempting to gather API data")
    start = (int(page) - 1) * 20
    results = api_post_req(
        "rescue_group", start, default_filter, default_fields, True
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
            age=age,
            gender=gender,
            location=location,
            save_animal=save_animal,
            limits=[start, start+20],
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
    default_fields = ALL_FIELDS
    log.debug("Attempting to gather API data")
    results = api_post_req(
        "rescue_group", 0, animal_filter, default_fields
    )
    if results is not None:
        result_dict = json.loads(results)
        return render_template(
            "animal.html",
            results=result_dict,
            animal_id=animal_id,
            save_animal=save_animal,
            strip_tags=strip_tags,
        )
    else:
        return render_template("error.html")


@app.route("/save-animal/<animal_id>")
def save_animals(animal_id):
    """
    This function just responds to the browser URL
    localhost:8090/

    :return:        the rendered template "home.html"
    """
    save_animal(animal_id)


@app.route("/remove-animal/<animal_id>", methods=["GET", "POST"])
def remove_animals(animal_id):
    """
    This function just responds to the browser URL
    localhost:8090/

    :return:        the rendered template "home.html"
    """
    removed = remove_animal(animal_id)


def run():
    # app.add_api("my_api.yaml")
    app.run(debug=True, host="0.0.0.0", port=PORT)
