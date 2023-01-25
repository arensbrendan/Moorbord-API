from __future__ import print_function
import grpc
from python.proto_files.admin import admin_pb2
from python.proto_files.admin import admin_pb2_grpc
from dotenv import load_dotenv
import os
from decorators import database_connect

load_dotenv()



@database_connect
def add_user(request, db):
    print("Will try to call ...")
    # We are going to grab all usernames in user table
    sql = "SELECT username FROM user"
    ids = []
    db.execute(sql)
    usernames = db.fetchall()
    # Now we'll loop through them and grab the 6 digits after their initials
    for i in usernames:
        ids.append(int(i["username"][2::]))
    # Now we'll generate a username for the new user based off of their initials, and the next sequential 6 digit number
    username = request["firstname"][0] + request["lastname"][0] + str(max(ids) + 1)
    with grpc.insecure_channel(os.getenv("IP") + ':1') as channel:
        stub = admin_pb2_grpc.AdminCallStub(channel)
        # Send in request with appropriate data
        response = stub.AddUser(
            admin_pb2.AddRequest(username=username, first_name=request["firstname"], last_name=request["lastname"],
                                 user_password=request["user_password"], email=request["email"],
                                 role_id=request["role"]))
    return response



@database_connect
def remove_user(request, db):
    with grpc.insecure_channel(os.getenv("IP") + ':1') as channel:
        stub = admin_pb2_grpc.AdminCallStub(channel)
        # Send remove user request
        response = stub.RemoveUser(admin_pb2.RemoveRequest(user_id=request["user_id"]))
    return response
