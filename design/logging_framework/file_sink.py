from log_sink import LogSink

class FileSink(LogSink):
    def __init__(self, filepath: str):
        self._file = open(filepath, "a", encoding="utf-8")

    def write(self, formatted: str):
        self._file.write(formatted + "\n")
        self._file.flush()

    def close(self):
        self._file.close()

