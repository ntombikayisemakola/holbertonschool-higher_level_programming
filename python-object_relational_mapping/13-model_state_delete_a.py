#!/usr/bin/python3
"""
Script to delete all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server using SQLAlchemy
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{db_name}')

    # Bind the engine to the metadata of the Base class so that the declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine

    # Create a session maker instance
    DBSession = sessionmaker(bind=engine)

    # Create a session
    session = DBSession()

    # Query for all State objects whose name contains the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each State object found
    for state in states_with_a:
        session.delete(state)

    # Commit the transaction to delete the objects from the database
    session.commit()

    # Close the session
    session.close()
