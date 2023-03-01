from __future__ import print_function
import grpc
from python.proto_files.room import room_pb2
from python.proto_files.room import room_pb2_grpc
from dotenv import load_dotenv
import os

load_dotenv()

ip = os.getenv("PRIVATE_IP") + ":5"


def add_room(request):
    with grpc.insecure_channel(ip) as channel:
        stub = room_pb2_grpc.RoomCallStub(channel)
        response = stub.AddRoom(
            room_pb2.AddRoomRequest(room_name=request["room_name"], room_length=request["room_length"], room_width=request["room_width"])
        )
    return response


def remove_room(request):
    with grpc.insecure_channel(ip) as channel:
        stub = room_pb2_grpc.RoomCallStub(channel)
        response = stub.RemoveRoom(
            room_pb2.RemoveRoomRequest(room_id=request["room_id"])
        )
    return response