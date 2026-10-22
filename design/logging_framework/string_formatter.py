from log_formatter import LogFormatter
from log_record import LogRecord

class StringFormatter(LogFormatter):
    def format(self, log_record: LogRecord)->str:
        return f"{log_record.timestamp}:[{log_record.log_level}]:{log_record.thread_name}:{log_record.message}"