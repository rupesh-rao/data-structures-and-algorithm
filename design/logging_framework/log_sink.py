from abc import ABC, abstractmethod

class LogSink(ABC):
    @abstractmethod
    def write(self, formatted: str):
        pass