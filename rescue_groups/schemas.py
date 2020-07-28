from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column,
    DateTime,
    Text,
    Integer,
    func,
)
from rescue_groups.models.parser import strip_tags
from rescue_groups.utils.logger import log
from rescue_groups.utils.all_fields import SAVED_FIELDS

from typing import Mapping, Any

import sqlalchemy
import os

URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg2://admin:postgres@api_app_postgres:5432/api_data",
)
log.info("Connecting to postgres hardcoded")

engine = sqlalchemy.create_engine(URL, client_encoding="utf8")

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Animals(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    location = Column(Text, nullable=True)
    eye_color = Column(Text, nullable=True)
    color = Column(Text, nullable=True)
    name = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    thumbnail = Column(Text, nullable=True)
    age = Column(Text, nullable=True)
    sex = Column(Text, nullable=True)

    created_date = Column(DateTime, server_default=func.now())

    def to_dict(self):
        return self.__dict__

    def from_dict(self, animal_id: int, animal_data: Mapping[str, Any]) -> 'Animals':
        animal_dict = {"id": animal_id}
        for field in SAVED_FIELDS:
            field_data = animal_data.get(animal_id).get(field)
            db_field = Animals.mappings.get(field)
            if db_field == "description":
                animal_dict[db_field] = strip_tags(field_data)
            else:
                animal_dict[db_field] = field_data
        return Animals(**animal_dict)

    @property
    def mappings(self) -> Mapping[str, Any]:
        return {
            "locationPostalcode": "location",
            "animalEyeColor": "eye_color",
            "animalColor": "color",
            "animalName": "name",
            "animalDescription": "description",
            "animalGeneralAge": "age",
            "animalSex": "sex",
            "animalThumbnailUrl": "thumbnail",
        }


Base.metadata.create_all(engine)
