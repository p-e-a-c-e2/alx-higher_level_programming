#!/usr/bin/python3
"""
A script that changes the name of a State object from the database hbtn_0e_
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    fetch_objects = session.query(State).get(2)
    fetch_objects.name = "New Mexico"
    session.commit()
