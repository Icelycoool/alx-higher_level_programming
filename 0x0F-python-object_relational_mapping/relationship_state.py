#!/usr/bin/python3
"""Defines a State Class"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """
    State class that inherits from bas

    Attributes:
        id: The state id, primary key.
        name: The state name.
        cities: The State-City relationship.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
