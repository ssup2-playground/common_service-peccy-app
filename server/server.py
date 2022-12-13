import socket

from flask import Flask, jsonify, send_file
from flask_cors import CORS

from domain.entity.hobby import Hobby
from domain.service.hobby import HobbyService

# Init Server
server = Flask(__name__)
CORS(server)


# Info
@server.route("/infos/name")
def get_info_name():
    return jsonify({"name": "peccy"})


@server.route("/infos/picture")
def get_info_picture():
    return send_file("../assets/peccy.png", mimetype="image/png")


# Hobby
@server.route("/hobbies", methods=["GET"])
def list_hobbies():
    hobbies = []
    for hobby in HobbyService().list_hobbies():
        hobbies.append({"id": hobby.id, "name": hobby.name})
    return jsonify({"hobbies": hobbies})


@server.route("/hobbies", methods=["POST"])
def create_hobby():
    hobby = HobbyService().create_hobby(Hobby(0, "test"))
    return jsonify({"id": hobby.id, "name": hobby.name})


@server.route("/hobbies/<hobby_id>", methods=["GET"])
def get_hobby(hobby_id):
    hobby = HobbyService().get_hobby(hobby_id)
    return jsonify({"id": hobby.id, "name": hobby.name})


@server.route("/hobbies/<hobby_id>", methods=["DELETE"])
def delete_hobby(hobby_id):
    HobbyService().delete_hobby(hobby_id)
    return jsonify({})

# Health
@server.route("/healthz")
def get_healthz():
    return '{"status":"UP"}'

# Debug
@server.route("/debugs/hostname")
def get_hostname():
    return socket.gethostname()


# Run
def run():
    server.run(host="0.0.0.0", port=80, debug=True)
