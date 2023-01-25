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
        username, firstname, lastname, password, email, role_id = request.username, request.first_name, request.last_name, request.user_password, request.email, request.role_id
        try:
            sql = "INSERT INTO new.user(username, first_name, last_name, email, role_id) VALUES('%s', '%s', '%s', " \
                  "'%s', '%s') as message" % (username, firstname, lastname, email, role_id)
            db.execute(sql)
            sql = "SELECT user_id FROM user WHERE username = '%s'" % username
            db.execute(sql)
            uid = db.fetchall()[0]["user_id"]
            sql = "INSERT INTO login VALUES('%s', '%s')" % (uid, password)
            db.execute(sql)
            return admin_pb2.AddReply(message="User Added", status_code=200)
        except Exception as e:
            return admin_pb2.AddReply(error=str(e), status_code = 400)

    @database_connect
    @block
    def RemoveUser(self, db, request, context):
        user_id = request.user_id
        try:
            sql = "SELECT * FROM user WHERE user_id = '%s'" % user_id
            db.execute(sql)
            if db.fetchall():
                sql = "DELETE FROM login WHERE user_id = '%s'" % user_id
                db.execute(sql)
                sql = "DELETE FROM user WHERE user_id = '%s'" % user_id
                db.execute(sql)
                return admin_pb2.RemoveReply(message="User removed", status_code=200)
            else:
                raise ValueError("That user_id does not exist in the login")
        except ValueError as v:
            return admin_pb2.RemoveReply(error=str(v), status_code=404)
        except Exception as e:
            return admin_pb2.RemoveReply(error=str(e), status_code=400)


def serve():
    port = '1'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    admin_pb2_grpc.add_AdminCallServicer_to_server(AdminCall(), server)
    server.add_insecure_port(os.getenv("IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
