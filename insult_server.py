import grpc
import grpc_tools
import demo_pb2_grpc
import demo_pb2
from concurrent import futures


class Insult(demo_pb2_grpc.InsultServicer):
    def InsultPerson(self, request, context):
        names = {
            "Trey": "You're really not that smart",
            "Clayton": "You look stupid in those glasses",
            "Mitchell": "Relax, man, WWIII hasn't started yet",
            "Michael": "You have a big forehead"
        }
        return demo_pb2.InsultReply(insult=names[request.name])


def serve():
    port = '3'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_InsultServicer_to_server(Insult(), server)
    server.add_insecure_port('192.168.56.1:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
