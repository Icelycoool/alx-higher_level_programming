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
        .filter(State.id == City.state_id)

    for c in cities:
        print("{}: ({}) {}".format(c.State.name, c.City.id, c.City.name))

    session.close
