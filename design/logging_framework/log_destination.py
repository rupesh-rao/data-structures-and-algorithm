import threading
import sys

from log_record import LogRecord
from log_formatter import LogFormatter
from log_sink import LogSink
from log_level import LogLevel

class LogDestination:
    def __init__(self, formatter: LogFormatter, sink: LogSink, log_level: LogLevel):
        self._formatter = formatter
        self._sink = sink
        self._log_level = log_level
        self._lock = threading.Lock()

    def write(self, log_record: LogRecord):
        if log_record.log_level < self._log_level:
            return

        formatted = self._formatter.format(log_record)

        with self._lock:
            try:
                self._sink.write(formatted)
            except Exception as e:
                sys.stderr.write(f"logger: sink write failed: {e}\n")


