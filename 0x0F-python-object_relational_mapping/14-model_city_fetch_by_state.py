#!/usr/bin/python3
"""
A script that hat prints all City objects
from the database hbtn_0e_14_usa.
"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    cities = session.query(State, City) \
            .filter(State.id ==  City.state_id)

    for city in cities:
        print("{}: ({}) {}".format(city.State.name, city.City.id, city.City.name))

    session.close
