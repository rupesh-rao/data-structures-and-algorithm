from abc import ABC, abstractmethod
from log_record import LogRecord

class LogFormatter(ABC):
    @abstractmethod
    def format(self, log_record: LogRecord):
        pass