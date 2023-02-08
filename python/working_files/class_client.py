from __future__ import print_function
import grpc
from python.proto_files.class_files import class_pb2
from python.proto_files.class_files import class_pb2_grpc
from dotenv import load_dotenv
import os

load_dotenv()

ip = os.getenv("IP") + ":3"


def add_class(request):
    with grpc.insecure_channel(ip) as channel:
        stub = class_pb2_grpc.ClassCallStub(channel)
        response = stub.AddClass(
            class_pb2.AddClassRequest(teacher_username=request["teacher_username"], class_name=request["class_name"],
                                      hour=request["hour"]))
    return response


def remove_class(request):
    with grpc.insecure_channel(ip) as channel:
        stub = class_pb2_grpc.ClassCallStub(channel)
        response = stub.RemoveClass(
            class_pb2.RemoveClassRequest(class_id=request["class_id"])
        )
    return response


def add_user_to_class(request):
    with grpc.insecure_channel(ip) as channel:
        stub = class_pb2_grpc.ClassCallStub(channel)
        response = stub.AddUserToClass(
            class_pb2.AddUserToClassRequest(class_id=request["class_id"], username=request["username"])
        )
    return response


def remove_user_from_class(request):
    with grpc.insecure_channel(ip) as channel:
        stub = class_pb2_grpc.ClassCallStub(channel)
        response = stub.RemoveUserFromClass(
            class_pb2.RemoveUserFromClassRequest(class_id=request["class_id"], username=request["username"])
        )
    return response


def get_all_users_from_class(request):
    with grpc.insecure_channel(ip) as channel:
        stub = class_pb2_grpc.ClassCallStub(channel)
        response = stub.GetAllUsersFromClass(
            class_pb2.GetAllUsersFromClassRequest(class_id=request["class_id"])
        )
    return response
