import sys
sys.path.insert(0, '../protos')

import grpc
import meter_pb2
import meter_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = meter_pb2_grpc.MeterReadingStub(channel)
        responses = stub.IssueMeterReading(meter_pb2.MeterReadingRequest())
        for response in responses:
            print(response)

if __name__ == "__main__":
    run()