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
app.config['JWT_TOKEN_LOCATION'] = {'headers', 'query_string'}

users = {
    "John Doe": {
        "username": "John Doe",
        "role": "user",
        "password": "1234"
    },
    "Tata Mia": {
        "username": "Tata Mia",
        "role": "admin",
        "password": "4321"
    },
    "Ellie Coptair": {
        "username": "Ellie Coptair",
        "role": "admin",
        "password": "2143"
    },
    "John Weak": {
        "username": "John Weak",
        "role": "admin",
        "password": "1432"
    },
    "Alice Liddell": {
        "username": "Alice Liddell",
        "role": "user",
        "password": "2341"
    }
}

for user in users:
    users[user]["password"] = ws.generate_password_hash(
        users[user]["password"])


@app.route("/basic-protected")
@auth.login_required
def basic():
    return ("Basic Auth: Access Granted")


@auth.verify_password
def verify_pass(username, password):
    print("tot")
    for user in users:
        if (username == users[user]["username"] and
                ws.check_password_hash(users[user]["password"], password)):
            return username
    return None


@app.route("/login", methods=['POST'])
def login():
    data = request.json
    if (verify_pass(data["username"], data["password"])):
        access_token = create_access_token(identity=data["username"])
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "wrong user or password"}), 400


@app.route("/jwt-protected")
@jwt_required()
def jwt_auth():
    return ("JWT Auth: Access Granted")


@app.route("/admin-only")
@jwt_required()
def access_admin():
    username = get_jwt_identity()
    if (users[username]["role"] == "admin"):
        return jsonify("Admin Access: Granted"), 200
    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run()


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
