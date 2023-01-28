import grpc
from python.proto_files.class_files import class_pb2
from python.proto_files.class_files import class_pb2_grpc
from concurrent import futures
from dotenv import load_dotenv
import os
from python.working_files.decorators import database_connect

load_dotenv()

class ClassCall(class_pb2_grpc.ClassCallServicer):
    @database_connect
    def AddClass(self, db, request, context):
        teacher_username, class_name, hour = request.teacher_username, request.class_name, request.hour
        try:
            sql = "SELECT user_id FROM user WHERE username = '%s'" % teacher_username
            db.execute(sql)
            user_id = db.fetchall()[0]
            if user_id:
                sql = "SELECT * FROM class WHERE hour = '%s' AND teacher_id = '%s'" % (hour, user_id["user_id"])
                db.execute(sql)
                if db.fetchall():
                    raise ValueError("That teacher is already teaching a class at that hour!")
                else:
                    sql = "INSERT INTO class(teacher_id, class_name, hour) VALUES('%s', '%s', '%s')" % (user_id["user_id"], class_name, hour)
                    db.execute(sql)
                    return class_pb2.RemoveClassReply(message="Class Created", status_code=200)
            else:
                raise ValueError("The username provided for the teacher does not exist")
        except ValueError as error:
            return class_pb2.RemoveClassReply(error=str(error), status_code=404)
        except Exception as error:
            return class_pb2.RemoveClassReply(error=str(error), status_code=400)

    @database_connect
    def RemoveClass(self, db, request, context):
        class_id = request.class_id
        try:
            sql = "SELECT * FROM class WHERE class_id = '%s'" % class_id
            db.execute(sql)
            if db.fetchall():
                sql = "DELETE FROM class WHERE class_id = '%s'" % class_id
                db.execute(sql)
                return class_pb2.RemoveClassReply(message="Class has been removed", status_code=200)
            else:
                raise ValueError("That class does not exist")
        except ValueError as v:
            return class_pb2.RemoveClassReply(error=str(v), status_code=404)
        except Exception as error:
            return class_pb2.RemoveClassReply(error=str(error), status_code=400)

def serve():
    # General service setup
    port = '3'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    class_pb2_grpc.add_ClassCallServicer_to_server(ClassCall(), server)
    server.add_insecure_port(os.getenv("IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
