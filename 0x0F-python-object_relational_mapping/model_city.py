#!/usr/bin/python3
"""Defines a cities class"""


from sqlalchemy import String, Integer, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    City class that inherits from the Base class

    Attributes:
        id (int): The id of the city.
        name (string): The name of the city
        state_id (int): The state id (foreignkey)
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
