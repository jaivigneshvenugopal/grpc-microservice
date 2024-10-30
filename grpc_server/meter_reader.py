import sys
sys.path.insert(0, '../models')

import csv
from typing import Iterable
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from meter_reading import MeterReading

class MeterReader():
    def __init__(self):
        self.csv_file_path: str = './data/meterusage.csv'
        self.csv_file_delimiter: str = ','
        self.raw_date_format: str =  "%Y-%m-%d %H:%M:%S"

    def get_protobuf_timestamp(self, raw_timestamp: str) -> Timestamp:
        datetime_timestamp = datetime.strptime(raw_timestamp, self.raw_date_format).timestamp()
        protobuf_timestamp = Timestamp(seconds=int(datetime_timestamp), nanos=int(datetime_timestamp % 1 * 1e9))

        return protobuf_timestamp
    
    def get_meter_reading_value(self, raw_meter_reading_value: str) -> float:
        meter_reading_value = float(raw_meter_reading_value)

        return meter_reading_value

    def get_readings(self) -> Iterable[MeterReading]: 
        with open(self.csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.csv_file_delimiter)

            for line_number, line_values in enumerate(csv_reader):
                if line_number == 0:
                    continue

                raw_timestamp, raw_meter_reading_value = line_values[0], line_values[1]
                protobuf_timestamp = self.get_protobuf_timestamp(raw_timestamp)
                meter_reading_value = self.get_meter_reading_value(raw_meter_reading_value)

                meter_reading = MeterReading(timestamp=protobuf_timestamp, meter_reading_value=meter_reading_value)
                
                yield meter_reading