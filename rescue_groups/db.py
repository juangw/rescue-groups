from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (
    Column,
    DateTime,
    Text,
    Integer,
    func,
    ForeignKey,
)
from rescue_groups.models.parser import strip_tags
from rescue_groups.utils.logger import log

from typing import Mapping, Any

import sqlalchemy
import os

URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg2://admin:postgres@api_app_postgres:5432/api_data",
)
log.info("Connecting to postgres")

engine = sqlalchemy.create_engine(URL, client_encoding="utf8")

Base = declarative_base()
session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)


class Animals(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    user_id = Column(Text, ForeignKey("users.id"), index=True, nullable=False)
    location = Column(Text, nullable=True)
    eye_color = Column(Text, nullable=True)
    color = Column(Text, nullable=True)
    name = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    thumbnail = Column(Text, nullable=True)
    age = Column(Text, nullable=True)
    sex = Column(Text, nullable=True)
    created_date = Column(DateTime, server_default=func.now())

    _db_mappings = {
        "animalID": "id",
        "userID": "user_id",
        "locationPostalcode": "location",
        "animalEyeColor": "eye_color",
        "animalColor": "color",
        "animalName": "name",
        "animalDescription": "description",
        "animalGeneralAge": "age",
        "animalSex": "sex",
        "animalThumbnailUrl": "thumbnail",
    }
    _db_fields = [
        "animalID",
        "userID",
        "animalName",
        "animalSex",
        "animalGeneralAge",
        "animalDescription",
        "locationPostalcode",
        "animalColor",
        "animalEyeColor",
        "animalThumbnailUrl",
    ]

    def to_dict(self) -> Mapping[str, Any]:
        return self.__dict__

    def from_dict(self, animal_data: Mapping[str, Any]):
        for field in self._db_fields:
            field_data = animal_data.get(field)
            db_field = self.map_field(field)
            if db_field == "description":
                setattr(self, db_field, strip_tags(field_data))
            else:
                setattr(self, db_field, field_data)

    def map_field(self, value: str) -> str:
        return self._db_mappings[value]


class Users(Base):
    __tablename__ = "users"

    id = Column(Text, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    profile_pic = Column(Text, nullable=True)
    created_date = Column(DateTime, server_default=func.now())

    def to_dict(self) -> Mapping[str, Any]:
        return self.__dict__

    def from_dict(self, user_data: Mapping[str, Any]):
        self.id = user_data["id"]
        self.name = user_data["name"]
        self.email = user_data["email"]
        self.profile_pic = user_data["profile_pic"]

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


def init_db():
    Base.metadata.create_all(engine)
