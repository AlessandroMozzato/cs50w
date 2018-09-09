import os

from flask import Flask, session, render_template, request, jsonify
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

@app.route("/", methods=["GET", "POST"])
def index():
    session['user_id'] = 'logged_out'

    if (request.method == "POST") & (request.form.get("type") == 'register'):
        username = request.form.get("username")
        password = request.form.get("password")

        if db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).rowcount > 0:
            return render_template("error.html", message="username already exists")

        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
            {"username": username, "password": password})
        db.commit()

        user = (db.execute("SELECT * FROM users WHERE (username = :username)", {"username": username}).fetchone())
        session['user_id'] = user['id']
        session['username'] = username

        return render_template('index.html', type='register')

    if (request.method == "POST") & (request.form.get("type") == 'login'):
        username = request.form.get("username")
        password = request.form.get("password")

        if (db.execute("SELECT * FROM users WHERE (username = :username)", 
                {"username": username}).rowcount) == 0:
            return render_template("error.html", message="username does not exist")

        if (db.execute("SELECT * FROM users WHERE (username = :username AND password = :password)", 
                {"username": username, "password": password}).rowcount) == 0:
            return render_template("error.html", message="password incorrect")
            
        if db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
            {"username": username, "password": password}).rowcount == 1:
            
            user = (db.execute("SELECT * FROM users WHERE (username = :username)", {"username": username}).fetchone())
            session['user_id'] = user['id']
            session['username'] = username

            return render_template('index.html', type='login')

    return render_template('index.html')

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

@app.route("/book/<int:book_id>", methods=["GET", "POST"])
def book(book_id):
    book = db.execute("SELECT * FROM books WHERE id = :id", {"id": book_id}).fetchone()
    reviews = db.execute("SELECT * FROM reviews WHERE book_id = :book_id", {"book_id": book_id}).fetchall()

    if book is None:
        return render_template("error.html", message="No such book.")

    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": grkey, "isbns": book.isbn})
    reviews_count = res.json()['books'][0]['reviews_count']
    average_rating = res.json()['books'][0]['average_rating']

    if (request.method == "POST"):
        if session['user_id'] in [review.user_id for review in reviews]:
            return render_template("error.html", message="You already have a review for this book.")
        
        newreview = request.form.get("newreview")

        db.execute("INSERT INTO reviews (user_id, book_id, review) VALUES (:user_id, :book_id, :review)",
            {"user_id":session["user_id"], "book_id":book_id, "review":newreview})
        db.commit()

        reviews = db.execute("SELECT * FROM reviews WHERE book_id = :book_id", {"book_id": book_id}).fetchall()
        return render_template("book.html", book=book, reviews_count=reviews_count, 
            average_rating=average_rating, reviews=reviews)

    return render_template("book.html", book=book, reviews_count=reviews_count, 
        average_rating=average_rating, reviews=reviews)

@app.route("/api/<string:isbn>")
def book_api(isbn):
    book = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": isbn}).fetchone()

    if book is None:
        return jsonify({"error": "The book is not in the database"}), 404

    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": grkey, "isbns": book.isbn})
    reviews_count = res.json()['books'][0]['reviews_count']
    average_rating = res.json()['books'][0]['average_rating']

    return jsonify({
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "isbn": book.isbn,
        "review_count": reviews_count,
        "average_score": average_rating
        })
