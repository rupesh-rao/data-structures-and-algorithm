from log_sink import LogSink

class ConsoleSink(LogSink):
    def write(self, formatted: str):
        print(formatted)