from pydantic import BaseModel, ConfigDict
from google.protobuf.timestamp_pb2 import Timestamp

class MeterReading(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    timestamp: Timestamp
    meter_reading_value: float