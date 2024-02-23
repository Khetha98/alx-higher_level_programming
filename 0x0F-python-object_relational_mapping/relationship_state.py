#!/usr/bin/python3
"Module as a class definition State"

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

themetadata = MetaData()
Base = declarative_base(metadata=themetadata)

class State(Base):
    """Class for the State"""
    __tablename = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
