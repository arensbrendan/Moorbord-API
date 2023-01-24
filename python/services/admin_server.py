import grpc
from python.proto_files.admin import admin_pb2
from python.proto_files.admin import admin_pb2_grpc
from concurrent import futures
from dotenv import load_dotenv
import os
from python.working_files.decorators import database_connect, block

load_dotenv()


class AdminCall(admin_pb2_grpc.AdminCallServicer):
    @database_connect
    @block
    def AddUser(self, db, request, context):
        username, firstname, lastname, email, role_id = request.username, request.firstname, request.lastname, request.email, request.role_id
        try:
            db.callproc("add_user", [username, firstname, lastname, email, role_id])
            results = db.fetchall()[0]
            return admin_pb2.AddReply(message="User Added")
        except Exception as e:
            return admin_pb2.AddReply(message=str(e))


def serve():
    port = '1'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    admin_pb2_grpc.add_AdminCallServicer_to_server(AdminCall(), server)
    server.add_insecure_port(os.getenv("IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
