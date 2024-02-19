#!/usr/bin/python3
""" prints the State object with name as argument from database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    new_inst = session.query(State).filter_by(name='Louisiana').first()
    print(new_inst.id)
    session.commit()
