import grpc
from proto_files import demo_pb2_grpc
from proto_files import demo_pb2
from concurrent import futures
import os
from dotenv import load_dotenv

load_dotenv()


class Test(demo_pb2_grpc.TestServicer):
    def Test(self, request, context):
        return demo_pb2.TestReply(reply='Test Successful')


def serve():
    port = '2'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_TestServicer_to_server(Test(), server)
    server.add_insecure_port(os.getenv("TREY_LAPTOP_IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
