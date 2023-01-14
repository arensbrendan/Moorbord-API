import grpc
import grpc_tools
import demo_pb2_grpc
import demo_pb2
from concurrent import futures


class HelloWorld(demo_pb2_grpc.HelloWorldServicer):
    def SayHello(self, request, context):
        print('hit')
        return demo_pb2.HelloReply(message="Hello %s" % request.name)


def serve():
    port = '1'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_HelloWorldServicer_to_server(HelloWorld(), server)
    server.add_insecure_port('localhost:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
