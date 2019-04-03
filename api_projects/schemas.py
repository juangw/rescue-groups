from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column,
    DateTime,
    Text,
    Integer,
    func,
)
from api_projects.server import log

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

    animal_id = Column(Integer, primary_key=True)
    zip_code = Column(Integer, nullable=False)
    phone_number = Column(Text)
    eye_color = Column(Text)
    color = Column(Text)
    name = Column(Text)
    cost = Column(Text)
    age = Column(Text)
    sex = Column(Text)

    created_date = Column(DateTime, server_default=func.now())

    def to_dict(self):
        return self.__dict__


Base.metadata.create_all(engine)
