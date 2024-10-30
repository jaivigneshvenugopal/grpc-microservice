import sys
sys.path.insert(0, '../protos')

import grpc
import time
import json
import uvicorn
import asyncio
import meter_pb2
import meter_pb2_grpc
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
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

async def stream_meter_readings():
    with grpc.insecure_channel("grpc_server:50051") as channel:
        stub = meter_pb2_grpc.MeterReadingStub(channel)
        meter_reading_responses = stub.IssueMeterReading(meter_pb2.MeterReadingRequest())
        for meter_reading_response in meter_reading_responses:
            yield json.dumps(MessageToDict(meter_reading_response))
            await asyncio.sleep(0.01)

@app.get("/")
async def root():
    return StreamingResponse(stream_meter_readings(), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
