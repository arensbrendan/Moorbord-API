import grpc
import grpc_tools
import demo_pb2_grpc
import demo_pb2
from concurrent import futures
import pymysql


class DatabaseCall(demo_pb2_grpc.DatabaseCallServicer):
    def DBCall(self, request, context):
        conn = pymysql.connect(host='153.91.111.212',
                               user="api",
                               password="",
                               database='morboord',
                               cursorclass=pymysql.cursors.DictCursor)
        print('hit')
        with conn.cursor() as db:
            sql = "SELECT last_name FROM student WHERE first_name = '%s'" % request.firstname
            db.execute(sql)
            lastname = db.fetchall()[0]["last_name"]
            return demo_pb2.DatabaseReply(lastname='The last name is %s' % lastname)

    def InfoFromID(self, request, context):
        conn = pymysql.connect(host='153.91.111.212',
                               user="api",
                               password="",
                               database='morboord',
                               cursorclass=pymysql.cursors.DictCursor)
        print('hit')
        print(request)
        with conn.cursor() as db:
            sql = "SELECT * FROM student where student_id = %s" % request.id
            db.execute(sql)
            results = db.fetchall()[0]
            firstname = results["first_name"]
            lastname = results["last_name"]
            return demo_pb2.InfoReply(name='The name is %s %s' % (firstname, lastname))


def serve():
    port = '4'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_DatabaseCallServicer_to_server(DatabaseCall(), server)
    server.add_insecure_port('192.168.56.1:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
