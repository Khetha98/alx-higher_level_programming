#!/usr/bin/python3
""" prints the State object with name as argument from database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    for inst in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(inst[0] + ": (" + str(inst[1]) + ") " + inst[2])
