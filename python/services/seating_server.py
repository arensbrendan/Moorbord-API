import grpc
from python.proto_files.seating import seating_pb2
from python.proto_files.seating import seating_pb2_grpc
from concurrent import futures
from dotenv import load_dotenv
import os
from python.working_files.decorators import database_connect
import json

load_dotenv()


class SeatingCall(seating_pb2_grpc.SeatingCallServicer):
    @database_connect
    def AddSeatingArrangement(self, db, request, context):
        class_id, arrangement = request.class_id, json.loads(request.arrangement)
        try:
            for i in arrangement:
                sql = "INSERT INTO chair(chair_x, chair_y, student_id, class_id) VALUES(%s, %s, %s, %s)" % (
                i["x"], i["y"], i["student_id"], class_id)
                db.execute(sql)
            # 200 for successful.  Even if they don't match, the code ran successfully
            return seating_pb2.AddChairToSeatingArrangementReply(message="The chairs have been added to that class",
                                                                 status_code=200)
        except Exception as e:
            # Generic answer returns a 400
            return seating_pb2.AddChairToSeatingArrangementReply(error=str(e), status_code=400)

    @database_connect
    def RemoveChairFromSeatingArrangement(self, db, request, context):
        chair_ids = json.loads(request.chair_ids)
        try:
            for i in chair_ids:
                sql = "DELETE FROM chair WHERE chair_id = %s" % i
                db.execute(sql)
            return seating_pb2.RemoveChairFromSeatingArrangementReply(message="The chairs have been deleted from that class",
                                                                      status_code=200)
        except Exception as e:
            return seating_pb2.RemoveChairFromSeatingArrangementReply(error=str(e), status_code=400)


def serve():
    # Generic Service Stuff
    port = '6'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    seating_pb2_grpc.add_SeatingCallServicer_to_server(SeatingCall(), server)
    server.add_insecure_port(os.getenv("PRIVATE_IP") + ':' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
