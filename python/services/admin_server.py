import grpc
from python.proto_files.admin import admin_pb2
from python.proto_files.admin import admin_pb2_grpc
from concurrent import futures
from dotenv import load_dotenv
import os
from python.working_files.decorators import database_connect

load_dotenv()


class AdminCall(admin_pb2_grpc.AdminCallServicer):
    @database_connect
    def AddUser(self, db, request, context):
        # Populate values sent in the request
        username, firstname, lastname, password, email, role_id = request.username, request.first_name, request.last_name, request.user_password, request.email, request.role_id
        try:
            # Insert all relevant data into the user table
            sql = "INSERT INTO new.user(username, first_name, last_name, email, role_id) VALUES('%s', '%s', '%s', " \
                  "'%s', '%s') as message" % (username, firstname, lastname, email, role_id)
            db.execute(sql)
            # Grab the new user_id that was generated
            sql = "SELECT user_id FROM user WHERE username = '%s'" % username
            db.execute(sql)
            uid = db.fetchall()[0]["user_id"]
            # Now populate the login table with the id and password attached
            sql = "INSERT INTO login VALUES('%s', '%s')" % (uid, password)
            db.execute(sql)
            # 200 is a successful error code
            return admin_pb2.AddReply(message="User Added", status_code=200)
        except Exception as e:
            # 400 is unsuccessful
            return admin_pb2.AddReply(error=str(e), status_code=400)

    @database_connect
    def RemoveUser(self, db, request, context):
        # Grab user id from request data
        user_id = request.user_id
        try:
            # Verifying that the user_id exists
            sql = "SELECT * FROM user WHERE user_id = '%s'" % user_id
            db.execute(sql)
            if db.fetchall():
                '''
                If the user_id exists, we will first drop it from the login table
                This is because of foreign key constraints.  Before deleting the root primary key, we must remove it from
                Any foreign key positions first
                '''
                sql = "DELETE FROM login WHERE user_id = '%s'" % user_id
                db.execute(sql)
                # After that, we delete the user from the user table
                sql = "DELETE FROM user WHERE user_id = '%s'" % user_id
                db.execute(sql)
                # 200 is successful
                return admin_pb2.RemoveReply(message="User removed", status_code=200)
            else:
                raise ValueError("That user_id does not exist in the login")
        except ValueError as v:
            # If the user doesn't exist, return 404 for not found
            return admin_pb2.RemoveReply(error=str(v), status_code=404)
        except Exception as e:
            # Generic error returns a 400
            return admin_pb2.RemoveReply(error=str(e), status_code=400)


def serve():
    # General service setup
    port = '1'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    admin_pb2_grpc.add_AdminCallServicer_to_server(AdminCall(), server)
    server.add_insecure_port(os.getenv("IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
