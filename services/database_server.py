import grpc
from proto_files import demo_pb2_grpc
from proto_files import demo_pb2
from concurrent import futures
import pymysql
from dotenv import load_dotenv
import os
from working_files.decorators import database_connect, block, log

load_dotenv()


class DatabaseCall(demo_pb2_grpc.DatabaseCallServicer):
    @database_connect
    @block
    @log(__file__)
    def DBCall(self, conn, request, context):
        try:
            with conn.cursor() as db:
                sql = "SELECT last_name FROM student WHERE first_name = '%s'" % request.firstname
                db.execute(sql)
                lastname = db.fetchall()[0]["last_name"]
                var = demo_pb2.DatabaseReply(lastname='The last name is %s' % lastname)
                print(var)
                return var
        except Exception as error:
            return str(error)

    @database_connect
    @block
    @log(__file__)
    def InfoFromID(self, conn, request, context):
        print(request)
        with conn.cursor() as db:
            sql = "SELECT * FROM student where student_id = %s" % request.id
            db.execute(sql)
            results = db.fetchall()[0]
            firstname = results["first_name"]
            lastname = results["last_name"]
            return demo_pb2.InfoReply(name='The name is %s %s' % (firstname, lastname))


def serve():
    port = '1'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_DatabaseCallServicer_to_server(DatabaseCall(), server)
    server.add_insecure_port(os.getenv("IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
