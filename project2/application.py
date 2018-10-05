import os

from flask import Flask, session, render_template, request, jsonify, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

chatnames = {}
chatsfull = {}

@app.route("/")
def index():
	path = url_for('index')
	return render_template('index.html', chatnames=chatnames, chatsfull=chatsfull)

@socketio.on("create chat")
def vote(data):
	chatname = data["chatname"]
	if chatname in chatnames:
		chatname = 'Raise:error'
	else:
		chatnames[chatname] = chatname
	emit("all chats", chatname, broadcast=True)


@socketio.on("send message")
def message(data):
	print(data)
	data = data['message'].split('::')
	message = data[0]
	chatname = data[1]

	if chatname in chatsfull.keys():
		chatsfull[chatname].append(message)
		if len(chatsfull[chatname])>100:
			chatsfull[chatname].pop(0)
	else:
		chatsfull[chatname] = [message]
	emit("messages", message, broadcast=True)

@app.route("/chats/<string:chatname>")
def chat(chatname):
    return render_template('index.html', chatnames=chatnames, chatname=chatname, chatsfull=chatsfull)

@app.route("/chatsapi", methods=['GET','POST'])
def chatapi():
	return jsonify(chatsfull)