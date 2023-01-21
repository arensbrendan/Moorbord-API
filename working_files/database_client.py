from __future__ import print_function
import grpc
from proto_files.database import database_call_pb2
from proto_files.database import database_call_pb2_grpc
from dotenv import load_dotenv
import os
from decorators import block
from json import dumps

load_dotenv()


@block
def login(request):
    print("Will try to call ...")
    with grpc.insecure_channel(os.getenv("IP") + ':1') as channel:
        stub = database_call_pb2_grpc.DatabaseCallStub(channel)
        response = stub.Login(database_call_pb2.LoginRequest(username=request['username'], password=request['password'], body=dumps(request)))
    return response
