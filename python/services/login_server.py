import grpc
from python.proto_files.login import login_pb2
from python.proto_files.login import login_pb2_grpc
from concurrent import futures
from dotenv import load_dotenv
import os
from python.working_files.decorators import database_connect, block

load_dotenv()


class LoginCall(login_pb2_grpc.LoginCallServicer):
    @database_connect
    @block
    def Login(self, db, request, context):
        user_input = request.username
        password_input = request.password
        try:
            sql = "SELECT user_id FROM user WHERE username = '%s'" % user_input
            db.execute(sql)
            uid = db.fetchall()
            if uid:
                uid = uid[0]["user_id"]
            else:
                raise ValueError("That user does not exist")
            sql = "SELECT password FROM login WHERE user_id = '%s'" % uid
            db.execute(sql)
            results = db.fetchall()[0]
            correct = True if results['password'] == password_input else False
            return login_pb2.LoginReply(correct=correct, status_code=200)
        except Exception as e:
            return login_pb2.LoginReply(error=str(e), status_code = 400)


def serve():
    port = '1'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    login_pb2_grpc.add_LoginCallServicer_to_server(LoginCall(), server)
    server.add_insecure_port(os.getenv("IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
