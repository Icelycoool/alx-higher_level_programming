#!/usr/bin/python3
"""
A scrip that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
