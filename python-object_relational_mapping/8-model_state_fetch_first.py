#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def main():
    """
    the fonction use to search good data
    """
    session = sessionmaker(engine)
    session = session()
    state = session.query(State).order_by(State.id).limit(1).one()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    main()
