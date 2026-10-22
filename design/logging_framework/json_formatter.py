from log_formatter import LogFormatter
from log_record import LogRecord
import json
from dataclasses import asdict

class JsonFormatter(LogFormatter):
    def format(self, log_record: LogRecord):
        return json.dumps(asdict(LogRecord))