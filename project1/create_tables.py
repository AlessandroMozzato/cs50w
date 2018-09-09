import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    # Create users table 
    db.execute("""
        DROP TABLE IF EXISTS users ;
        CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR NOT NULL,
        password VARCHAR NOT NULL)
    """)
    db.commit()

    # Create reviews table 
    db.execute("""
        DROP TABLE IF EXISTS reviews ;
        CREATE TABLE reviews (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        review VARCHAR NOT NULL)
    """)
    db.commit()

if __name__ == "__main__":
    main()