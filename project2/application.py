import os

from flask import Flask, session, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

chats = {"new": 0}

@app.route("/")
def index():
    return render_template('index.html', chats=chats)

@socketio.on("submit vote")
def vote(data):
    selection = data["selection"]
    chats[selection] += 1
    emit("vote totals", chats, broadcast=True)