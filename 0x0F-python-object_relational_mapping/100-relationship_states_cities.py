#!/usr/bin/python3
"""
A script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa: (100-relationship_states_cities.py).
"""


from sys import argv
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    session.add(new_state)
    session.add(new_city)

    session.commit()
    session.close()
