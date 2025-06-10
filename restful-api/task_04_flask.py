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
    dict_ret = {}
    if username in users:
        val = users[username]
        dict_ret["username"] = username
        for i in val:
            dict_ret[i] = val[i]
        return jsonify(data=dict_ret)
    else:
        return jsonify(data={"error": "User not found"}, status=400)


@app.route("/add_user", methods=['POST'])
def add_users():
    data_user = request.get_json()
    print(data.get['username'])
    returnval = {"message": "User added", "user": {}}
    if "username" in data.keys() and request.methode == 'POST':
        users[data["username"]] = data
        returnval["user"] = data
        return jsonify(data=returnval, status=201)
    else:
        return jsonify(data={"error": "User not found"}, status=400)


if __name__ == "__main__":
    app.run()
