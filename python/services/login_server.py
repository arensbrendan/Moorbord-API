import grpc
from python.proto_files.login import login_pb2
from python.proto_files.login import login_pb2_grpc
from concurrent import futures
from dotenv import load_dotenv
import os
from python.working_files.decorators import database_connect
import json
import asyncio

load_dotenv()


class LoginCall(login_pb2_grpc.LoginCallServicer):
    @database_connect
    async def Login(self, db, request, context):
        # Grab username and password from the request
        user_input, password_input = request.username, request.password
        try:
            # We want to first check that the user exists, and grab their UID
            sql = "SELECT user_id FROM user WHERE username = '%s'" % user_input
            db.execute(sql)
            uid = db.fetchall()
            if uid:
                uid = uid[0]["user_id"]
            else:
                raise ValueError("That user does not exist")
            # We're going to grab the password from login now
            sql = "SELECT password FROM login WHERE user_id = '%s'" % uid
            db.execute(sql)
            results = db.fetchall()[0]
            # True if the passwords match, otherwise False
            object = ""
            if password_input == results['password']:
                sql = "SELECT * from user WHERE user_id = '%s'" % uid
                db.execute(sql)
                object = db.fetchall()[0]
            else:
                raise Exception("The username/password is incorrect")
            # 200 for successful.  Even if they don't match, the code ran successfully
            return login_pb2.LoginReply(object=json.dumps(object), status_code=200)
        except Exception as e:
            # Generic answer returns a 400
            return login_pb2.LoginReply(error=str(e), status_code=400)


async def serve() -> None:
    # Generic Service Stuff
    port = '2'
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    login_pb2_grpc.add_LoginCallServicer_to_server(LoginCall(), server)
    server.add_insecure_port(os.getenv("IP") + ':' + port)
    await server.start()
    print("Server started, listening on " + port)
    await server.wait_for_termination()


if __name__ == "__main__":
    serve()
