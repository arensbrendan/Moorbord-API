from __future__ import print_function
import grpc
from python.proto_files.admin import admin_pb2
from python.proto_files.admin import admin_pb2_grpc
from dotenv import load_dotenv
import os
from decorators import block, database_connect
from json import dumps

load_dotenv()


@block
@database_connect
def add_user(request, db):
    print("Will try to call ...")
    sql = "SELECT username FROM user"
    ids = []
    db.execute(sql)
    usernames = db.fetchall()
    for i in usernames:
        ids.append(int(i["username"][2::]))
    username = request["firstname"][0] + request["lastname"][0] + str(max(ids) + 1)
    with grpc.insecure_channel(os.getenv("IP") + ':1') as channel:
        stub = admin_pb2_grpc.AdminCallStub(channel)
        response = stub.AddUser(admin_pb2.AddRequest(username=username, first_name=request["firstname"], last_name=request["lastname"], email=request["email"], role_id=request["role"]))
    return response
