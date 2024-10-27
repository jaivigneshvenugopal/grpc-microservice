from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MeterReadingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MeterReadingReply(_message.Message):
    __slots__ = ("timestamp", "meter_reading_value")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    METER_READING_VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    meter_reading_value: float
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., meter_reading_value: _Optional[float] = ...) -> None: ...
