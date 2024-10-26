from concurrent import futures
import logging

import grpc
import meter_pb2
import meter_pb2_grpc


class MeterReadingServicer(meter_pb2_grpc.MeterReadingServicer):
    def SayHello(self, request, context):
        return meter_pb2.MeterReadingReply(message="Hello, %s!" % request.name)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meter_pb2_grpc.add_MeterReadingServicer_to_server(MeterReadingServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()