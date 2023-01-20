from __future__ import print_function
import grpc
from proto_files.database import database_call_pb2
from proto_files.database import database_call_pb2_grpc
from dotenv import load_dotenv
import os
from decorators import log

load_dotenv()


def login(user_name, pass_word):
    try:
        print("Will try to call ...")
        with grpc.insecure_channel(os.getenv("TREY_DESKTOP_IP") + ':1') as channel:
            stub = database_call_pb2_grpc.DatabaseCallStub(channel)
            response = stub.Login(database_call_pb2.LoginRequest(username=user_name, password=pass_word))
        return response
    except Exception as e:
        return str(e)

