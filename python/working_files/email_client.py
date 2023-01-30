from __future__ import print_function
import grpc
from python.proto_files.email import email_pb2
from python.proto_files.email import email_pb2_grpc
from dotenv import load_dotenv
import os

load_dotenv()

ip = os.getenv("IP") + ":4"


def email_user(request):
    with grpc.insecure_channel(ip) as channel:
        stub = email_pb2_grpc.EmailCallStub(channel)
        response = stub.EmailUser(
            email_pb2.EmailUserRequest(username=request["username"], email_body=request["email_body"])
        )
    return response

