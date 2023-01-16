from __future__ import print_function

import logging

import grpc
import demo_pb2
import demo_pb2_grpc


def run(the_name):
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:1') as channel:
        stub = demo_pb2_grpc.HelloWorldStub(channel)
        response = stub.SayHello(demo_pb2.HelloRequest(name=the_name))
    return response.message


def run_goodbye(the_name):
    print("Will try to say goodbye ...")
    with grpc.insecure_channel('localhost:2') as channel:
        stub = demo_pb2_grpc.GoodbyeStub(channel)
        response = stub.SayGoodbye(demo_pb2.GoodbyeRequest(name=the_name))
    return response.message


def run_insult(the_name):
    print("Will try to insult ...")
    with grpc.insecure_channel('192.168.56.1:3') as channel:
        stub = demo_pb2_grpc.InsultStub(channel)
        response = stub.InsultPerson(demo_pb2.InsultRequest(name=the_name))
    return response.insult


def db_call(the_name):
    try:
        print("Will try to call ...")
        with grpc.insecure_channel('192.168.56.1:4') as channel:
            stub = demo_pb2_grpc.DatabaseCallStub(channel)
            response = stub.DBCall(demo_pb2.DatabaseRequest(firstname=the_name))
        return str(response.lastname)
    except Exception as e:
        return str(e)


def info_from_name(the_id):
    print("Will try to call ...")
    with grpc.insecure_channel('192.168.56.1:5') as channel:
        stub = demo_pb2_grpc.DatabaseCallStub(channel)
        response = stub.InfoFromID(demo_pb2.InfoRequest(id=the_id))
    return response.name
