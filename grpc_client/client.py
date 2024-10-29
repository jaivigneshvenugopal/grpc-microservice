import sys
sys.path.insert(0, '../protos')

import grpc
import meter_pb2
import meter_pb2_grpc
from google.protobuf.json_format import MessageToDict

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    output = []
    with grpc.insecure_channel("grpc_server:50051") as channel:
        stub = meter_pb2_grpc.MeterReadingStub(channel)
        responses = stub.IssueMeterReading(meter_pb2.MeterReadingRequest())
        for response in responses:
            output.append(MessageToDict(response))
    
    return output

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
