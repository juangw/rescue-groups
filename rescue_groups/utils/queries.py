from rescue_groups.db import session, Animals, Users
from rescue_groups.utils.call_rescue_group import animal_by_id_req
from rescue_groups.utils.logger import log

from typing import List, Any, Mapping
from flask_login import current_user
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import json


def save_animal(animal_id: int):
    """
        Saves a specific animal to database for storage

        :param animal_id: int of unique id for animal
    """
    log.info(f"Saving ID: {animal_id}")
    animals = json.loads(animal_by_id_req("rescue_group", animal_id))["data"]
    for data in animals.values():
        animal_data = data
        break

    animal = Animals()
    animal_data["userID"] = current_user.id
    animal.from_dict(animal_data)
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


def list_saved_animals() -> List[Animals]:
    """
        Lists all saved animals by the user
    """
    return session.query(Animals).filter(Animals.user_id == current_user.id).all()


def get_user_by_id(user_id: int) -> Users:
    try:
        return session.query(Users).filter(Users.id == user_id).one()
    except NoResultFound as e:
        log.error(f"No user with id: {user_id}", exc_info=e)
        return None


def insert_user(user_data: Mapping[str, Any]) -> Users:
    try:
        user = Users()
        user.from_dict(user_data)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except IntegrityError as e:
        message = "could not insert the job due to a constraint"
        log.error(message, e)
        return None
    except SQLAlchemyError as e:
        message = "could not insert the job due to a database error"
        log.error(message, e)
        return None
