import sys
sys.path.insert(0, '../protos')

import grpc
import uvicorn
import meter_pb2
import meter_pb2_grpc
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.protobuf.json_format import MessageToDict

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    meter_readings = []
    with grpc.insecure_channel("grpc_server:50051") as channel:
        stub = meter_pb2_grpc.MeterReadingStub(channel)
        meter_reading_responses = stub.IssueMeterReading(meter_pb2.MeterReadingRequest())
        for meter_reading_response in meter_reading_responses:
            meter_readings.append(MessageToDict(meter_reading_response))
    
    return meter_readings

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
