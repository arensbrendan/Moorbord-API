import grpc
from proto_files.database import database_call_pb2
from proto_files.database import database_call_pb2_grpc
from concurrent import futures
import pymysql
from dotenv import load_dotenv
import os
from working_files.decorators import database_connect, block, log

load_dotenv()


class DatabaseCall(database_call_pb2_grpc.DatabaseCallServicer):
    @database_connect
    @block
    # @log(__file__)
    def CheckLogin(self, db, request, context):
        password_user = request.username
        password_input = request.password
        db.callproc("login_test", [password_user])
        results = db.fetchall()[0]
        return database_call_pb2.LoginReply(correct=True if results['password'] == password_input else False)


def serve():
    port = '1'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    database_call_pb2_grpc.add_DatabaseCallServicer_to_server(DatabaseCall(), server)
    server.add_insecure_port(os.getenv("TREY_DESKTOP_IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
