from __future__ import print_function
import grpc
from python.proto_files.seating import seating_pb2
from python.proto_files.seating import seating_pb2_grpc
from dotenv import load_dotenv
import os
import json

load_dotenv()

ip = os.getenv("PRIVATE_IP") + ":6"


def add_seating_arrangement(request):
    with grpc.insecure_channel(ip) as channel:
        stub = seating_pb2_grpc.SeatingCallStub(channel)
        response = stub.AddSeatingArrangement(
            seating_pb2.AddSeatingArrangementRequest(class_id=request["class_id"], arrangement=json.dumps(request["arrangement"]))
        )
    return response
