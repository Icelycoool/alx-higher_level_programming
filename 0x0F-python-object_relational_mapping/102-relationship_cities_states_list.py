#!/usr/bin/python3
"""
A script that lists all City objects
from the database hbtn_0e_101_usa.
"""


from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
