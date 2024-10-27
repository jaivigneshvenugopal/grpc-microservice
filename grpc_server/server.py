import sys
sys.path.insert(0, '../protos')

import csv
import grpc
import logging
import meter_pb2
import meter_pb2_grpc

from concurrent import futures

from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime

class MeterReadingServicer(meter_pb2_grpc.MeterReadingServicer):
    def IssueMeterReading(self, request, context):
        with open('./data/meterusage.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line_number, line in enumerate(csv_reader):
                if line_number == 0:
                    continue
                raw_timestamp, raw_meter_reading_value = line[0], line[1]
                datetime_timestamp = datetime.strptime(raw_timestamp, "%Y-%m-%d %H:%M:%S").timestamp()
                protobuf_timestamp = Timestamp(seconds=int(datetime_timestamp), nanos=int(datetime_timestamp % 1 * 1e9))
                yield meter_pb2.MeterReadingReply(timestamp=protobuf_timestamp, meter_reading_value=float(raw_meter_reading_value))


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