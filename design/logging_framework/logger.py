from datetime import datetime
from threading import current_thread
from typing import Iterable

from log_level import LogLevel
from log_record import LogRecord
from log_destination import LogDestination



class Logger:
    def __init__(self, destinations: Iterable[LogDestination]):
        self.destinations: list[LogDestination] = list(destinations)

    def log(self, log_level: LogLevel, message: str):
        log_record = LogRecord(
            timestamp=datetime.now(),
            log_level=log_level,
            message=message,
            thread_name=current_thread().getName()
        )
        for destination in self.destinations:
            destination.write(log_record)

    def debug(self, message: str):
        self.log(LogLevel.DEBUG, message)

    def info(self, message: str):
        self.log(LogLevel.INFO, message)

    def warning(self, message: str):
        self.log(LogLevel.WARNING, message)

    def error(self, message: str):
        self.log(LogLevel.ERROR, message)

    def fatal(self, message: str):
        self.log(LogLevel.FATAL, message)
