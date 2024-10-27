import sys
sys.path.insert(0, '../protos')

import csv
import grpc
import logging
import meter_pb2
import meter_pb2_grpc

from concurrent import futures


class MeterReadingServicer(meter_pb2_grpc.MeterReadingServicer):
    def IssueMeterReading(self, request, context):
        with open('./data/meterusage.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line_number, line in enumerate(csv_reader):
                if line_number == 0:
                    print(f'Column names are {", ".join(line)}')
                else:
                    print(line)
                    timestamp, meter_reading_value = line[0], line[1]
                    yield meter_pb2.MeterReadingReply(timestamp=timestamp, meter_reading_value=meter_reading_value)


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