from __future__ import print_function
import grpc
from proto_files import demo_pb2
from proto_files import demo_pb2_grpc
from dotenv import load_dotenv
import os
from decorators import hit

load_dotenv()


@hit(__file__)
def db_call(the_name):
    try:
        print("Will try to call ...")
        with grpc.insecure_channel(os.getenv("IP") + ':1') as channel:
            stub = demo_pb2_grpc.DatabaseCallStub(channel)
            response = stub.DBCall(demo_pb2.DatabaseRequest(firstname=the_name))
        return str(response.lastname)
    except Exception as e:
        return str(e)


@hit(__file__)
def info_from_name(the_id):
    print("Will try to call ...")
    with grpc.insecure_channel(os.getenv("IP") + ':1') as channel:
        stub = demo_pb2_grpc.DatabaseCallStub(channel)
        response = stub.InfoFromID(demo_pb2.InfoRequest(id=the_id))
    return response.name
