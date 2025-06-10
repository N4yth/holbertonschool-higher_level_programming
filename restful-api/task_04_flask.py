#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

global users
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def jsoni():
    res = []
    for key in users.keys():
        res.append(key)
    return jsonify(res)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<string:username>")
def usepart(username):
    if username in users:
        return jsonify(message=user[username])
    else:
        return jsonify(message={"error": "User not found"}), 400


@app.route("/add_user", methods=['POST'])
def add_users():
    data_user = request.get_json()
    if data_user.get("username"):
        users[data_user["username"]] = data_user
        return jsonify(message={"message": "User added", "user": data_user}), 201
    else:
        return jsonify(message={"error": "User not found"}), 400


if __name__ == "__main__":
    app.run()
