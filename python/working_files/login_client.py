from __future__ import print_function
import grpc
from python.proto_files.login import login_pb2
from python.proto_files.login import login_pb2_grpc
from dotenv import load_dotenv
import os
from json import dumps

load_dotenv()


def login(request):
    print("Will try to call ...")
    with grpc.insecure_channel(os.getenv("IP") + ':1') as channel:
        stub = login_pb2_grpc.LoginCallStub(channel)
        # Sends in a login request with appropriate data
        response = stub.Login(
            login_pb2.LoginRequest(username=request['username'], password=request['password'], body=dumps(request)))
    return response
