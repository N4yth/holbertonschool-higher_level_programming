#!/usr/bin/env python3
import werkzeug.security as ws
from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import jwt as jjwt
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
jwt = JWTManager(app)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret"

users = {
    "JohnDoe": {
        "username": "JohnDoe",
        "role": "user",
        "password": ws.generate_password_hash("1234")
    },
    "TataMia": {
        "username": "TataMia",
        "role": "admin",
        "password": ws.generate_password_hash("4321")
    },
    "EllieCoptair": {
        "username": "EllieCoptair",
        "role": "admin",
        "password": ws.generate_password_hash("2143")
    },
    "JohnWeak": {
        "username": "JohnWeak",
        "role": "admin",
        "password": ws.generate_password_hash("1432")
    },
    "AliceLiddell": {
        "username": "AliceLiddell",
        "role": "user",
        "password": ws.generate_password_hash("2341")
    }
}

@auth.verify_password
def verify_pass(username, password):
    if (username in users):
        if (ws.check_password_hash(users[username]["password"], password)):
            return username


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=['POST'])
def login():
    data = request.json
    if not data.get("username") or not data.get("password"):
        return jsonify({"message": "user or password missing"}), 400
    if (verify_pass(data["username"], data["password"])):
        access_token = create_access_token(identity=data["username"])
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "wrong user or password"}), 401


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_auth():
    return ("JWT Auth: Access Granted")


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def access_admin():
    username = get_jwt_identity()
    if (username in users):
        if (users[username]["role"] == "admin"):
            return jsonify("Admin Access: Granted"), 200
    return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
