from rescue_groups.schemas import session, Animals
from rescue_groups.utils.call_rescue_group import animal_by_id_req
from rescue_groups.utils.logger import log

from typing import List, Any, Mapping


def save_animal(animal_id: int):
    """
        Saves a specific animal to database for storage

        :param animal_id: int of unique id for animal
    """
    log.info(f"Saving ID: {animal_id}")
    animals = animal_by_id_req("rescue_group", animal_id)
    for id, data in animals:
        animal_id = id
        animal_data = data
        break

    animal: Animals = Animals.from_dict(animal_id, animal_data)
    session.add(animal)
    try:
        session.commit()
    except Exception:
        session.rollback()


def remove_animal(animal_id: int):
    """
        Saves a specific animal to database for storage

        :param animal_id: int of unique id for animal
    """
    log.info(f"Removing ID: {animal_id}")
    session.query(Animals).filter(Animals.id == int(animal_id)).delete()
    try:
        session.commit()
    except Exception:
        session.rollback()


def list_saved_animals() -> List[Mapping[str, Any]]:
    """
        Lists all saved animals by the user
    """
    matches = session.query(Animals).filter().all()
    return matches
