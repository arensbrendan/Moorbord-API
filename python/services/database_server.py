import grpc
from proto_files.database import database_call_pb2
from python.proto_files.database import database_call_pb2_grpc
from concurrent import futures
from dotenv import load_dotenv
import os
from working_files.decorators import database_connect, block

load_dotenv()


class DatabaseCall(database_call_pb2_grpc.DatabaseCallServicer):
    @database_connect
    @block
    def Login(self, db, request, context):
        user_input = request.username
        password_input = request.password
        db.callproc("get_passwd_from_username", [user_input])
        results = db.fetchall()[0]
        return database_call_pb2.LoginReply(correct=True if results['password'] == password_input else False)


def serve():
    port = '1'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    database_call_pb2_grpc.add_DatabaseCallServicer_to_server(DatabaseCall(), server)
    server.add_insecure_port(os.getenv("IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
