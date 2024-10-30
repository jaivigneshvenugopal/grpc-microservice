import sys
sys.path.insert(0, '../protos')
sys.path.insert(0, '../models')

import grpc
import meter_pb2
import meter_pb2_grpc

from concurrent import futures

from meter_reader import MeterReader

class MeterReadingServicer(meter_pb2_grpc.MeterReadingServicer):
    def __init__(self):
        self.meter_reader = MeterReader()

    def IssueMeterReading(self, request, context):
        for reading in self.meter_reader.get_readings():
            meter_reading_reply = meter_pb2.MeterReadingReply(timestamp=reading.timestamp, meter_reading_value=reading.meter_reading_value) 
            yield meter_reading_reply

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meter_pb2_grpc.add_MeterReadingServicer_to_server(MeterReadingServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print(f"gRPC server started, listening on port:{port}")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()