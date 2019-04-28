from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column,
    DateTime,
    Text,
    Integer,
    func,
)
from api_projects.log import log

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
    cost = Column(Text, nullable=True)
    age = Column(Text, nullable=True)
    sex = Column(Text, nullable=True)

    created_date = Column(DateTime, server_default=func.now())

    def to_dict(self):
        return self.__dict__


Base.metadata.create_all(engine)
