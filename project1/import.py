import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():

    # Create books table 
    db.execute("""
        DROP TABLE IF EXISTS books ;
        CREATE TABLE books (
        id SERIAL PRIMARY KEY,
        isbn VARCHAR NOT NULL,
        title VARCHAR NOT NULL,
        author VARCHAR NOT NULL,
        year INTEGER NOT NULL)
    """)
    db.commit()

    # We read the csv and insert elements in the table
    f = open('books.csv')
    reader = csv.reader(f)
    next(reader)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                {"isbn": isbn, "title": title, "author":author, "year":int(year)})
    db.commit()

if __name__ == "__main__":
    main()