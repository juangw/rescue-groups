from api_projects.schemas import session, Animals
from src.rescue_group.models.parser import strip_tags
from src.rescue_group.utils.call_rescue_group import animal_by_id_req
from src.rescue_group.utils.all_fields import SAVED_FIELDS, FIELD_MAPPING
from api_projects.log import log

import json


def save_animal(animal_id):
    """
        Saves a specific animal to database for storage

        :param animal_id: int of unique id for animal
    """
    log.info(f"Saving ID: {animal_id}")
    animal = animal_by_id_req("rescue_group", animal_id)
    animal_data = json.loads(animal)["data"]
    animal_id = list(animal_data.keys())[0]
    animal_dict = {"id": animal_id}

    for field in SAVED_FIELDS:
        field_data = animal_data.get(animal_id).get(field)
        db_field = FIELD_MAPPING.get(field)
        if db_field == "description":
            animal_dict[db_field] = strip_tags(field_data)
        else:
            animal_dict[db_field] = field_data
    animal = Animals(**animal_dict)
    session.add(animal)
    try:
        session.commit()
        return True
    except Exception:
        session.rollback()
        return False


def remove_animal(animal_id):
    """
        Saves a specific animal to database for storage

        :param animal_id: int of unique id for animal
    """
    log.info(f"Removing ID: {animal_id}")
    session.query(
        Animals
    ).filter(
        Animals.id == int(animal_id)
    ).delete()
    try:
        session.commit()
        return True
    except Exception:
        session.rollback()
        return False


def list_saved_animals():
    """
        Lists all saved animals by the user
    """
    matches = session.query(Animals).filter().all()
    return matches
