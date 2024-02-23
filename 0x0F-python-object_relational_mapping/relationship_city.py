#!/usr/bin/python3
"""It has a class for City"""
from relationship_state import Base
from sqlalchemy import Column, String, ForeignKey, Integer


class City(Base):
    """Class for the city definition"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
