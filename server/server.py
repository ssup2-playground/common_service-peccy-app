import socket
from flask import Flask, jsonify
from flask_cors import CORS
from domain.entity.hobby import Hobby
from domain.service.hobby import HobbyService

# Init Server
server = Flask(__name__)
CORS(server)


# Meta
@server.route("/meta/name")
def get_app_name():
    return "My app server"


@server.route("/meta/hostname")
def get_hostname():
    return socket.gethostname()


# Hobby
@server.route("/v1/hobbies", methods=["GET"])
def list_hobbies():
    hobbies = []
    for hobby in HobbyService().list_hobbies():
        hobbies.append({"id": hobby.id, "name": hobby.name})
    return jsonify({"hobbies": hobbies})


@server.route("/v1/hobbies", methods=["POST"])
def create_hobby():
    hobby = HobbyService().create_hobby(Hobby(0, "test"))
    return jsonify({"id": hobby.id, "name": hobby.name})


@server.route("/v1/hobbies/<hobby_id>", methods=["GET"])
def get_hobby(hobby_id):
    hobby = HobbyService().get_hobby(hobby_id)
    return jsonify({"id": hobby.id, "name": hobby.name})


@server.route("/v1/hobbies/<hobby_id>", methods=["DELETE"])
def delete_hobby(hobby_id):
    HobbyService().delete_hobby(hobby_id)
    return jsonify({})


# Run
def run():
    server.run(host="0.0.0.0", port=80, debug=True)
