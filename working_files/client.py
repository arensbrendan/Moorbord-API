from __future__ import print_function
import grpc
from proto_files import demo_pb2
from proto_files import demo_pb2_grpc
from dotenv import load_dotenv
import os
from decorators import log

load_dotenv()


@log(__file__)
def call_database(the_name):
    try:
        print("Will try to call ...")
        with grpc.insecure_channel(os.getenv("TREY_DESKTOP_IP") + ':1') as channel:
            stub = demo_pb2_grpc.DatabaseCallStub(channel)
            response = stub.DBCall(demo_pb2.DatabaseRequest(firstname=the_name))
        return str(response.lastname)
    except Exception as e:
        return str(e)


@log(__file__)
def get_student_info_from_name(the_id):
    print("Will try to call ...")
    with grpc.insecure_channel(os.getenv("TREY_DESKTOP_IP") + ':1') as channel:
        stub = demo_pb2_grpc.DatabaseCallStub(channel)
        response = stub.InfoFromID(demo_pb2.InfoRequest(id=the_id))
    return response.name


@log(__file__)
def test_connection(word):
    print("Will try to call ...")
    with grpc.insecure_channel(os.getenv("TREY_DESKTOP_IP") + ':2') as channel:
        stub = demo_pb2_grpc.TestStub(channel)
        response = stub.Test(demo_pb2.TestRequest(word=word))
    return response.reply
