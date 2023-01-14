import grpc
import grpc_tools
import demo_pb2_grpc
import demo_pb2
from concurrent import futures


class Goodbye(demo_pb2_grpc.GoodbyeServicer):
    def SayGoodbye(self, request, context):
        return demo_pb2.GoodbyeReply(message='Goodbye %s' % request.name)


def serve():
    port = '2'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_GoodbyeServicer_to_server(Goodbye(), server)
    server.add_insecure_port('localhost:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
