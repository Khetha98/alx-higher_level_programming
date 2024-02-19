#!/usr/bin/python3
""" prints the State object with name as argument from database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(City, State).join(State)

    for c, s in results.all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))

    session.commit()
    session.close()
