import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

grkey = 'O5rPbEJ5Y2O1jbWJppuBA'

@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/search/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        title = request.form.get("title")
        print(title)
        title = "%"+title+"%"
        books = db.execute("""
                    SELECT * 
                    FROM books 
                    WHERE 
                        (title LIKE :title)
                        OR (author LIKE :title)
                        OR (isbn LIKE :title)
                    """, {"title":title}).fetchall() 

        if len(books) == 0:
            return render_template("error.html", message="No books match the title author or isbn.")
        else:
            return render_template("search.html", books=books)       
    return render_template("search.html", books=None)

@app.route("/book/<int:book_id>")
def book(book_id):
    book = db.execute("SELECT * FROM books WHERE id = :id", {"id": book_id}).fetchone()
    if book is None:
        return render_template("error.html", message="No such book.")

    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": grkey, "isbns": book.isbn})
    reviews_count = res.json()['books'][0]['reviews_count']
    average_rating = res.json()['books'][0]['average_rating']
    return render_template("book.html", book=book, reviews_count=reviews_count, average_rating=average_rating)
