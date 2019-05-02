from api_projects.schemas import session, Animals
from src.rescue_group.utils.call_rescue_group import animal_by_id_req


def save_animal(animal_id):
    """
        Saves a specific animal to database for storage

        :param animal_id: int of unique id for animal
    """
    animal_data = animal_by_id_req("rescue_group", str(animal_id))
    print(animal_data)
    # animal = Animals()
    # session.add(animal)
    # matches = session.query(Animals).filter().all()
    # for match in matches:
    #     print(match.id, match.location)


def list_saved_animals():
    """
    """
    pass

if __name__ == '__main__':
    save_animal(14247860)
