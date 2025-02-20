import logging.config
import time
import json


class JsonFormatter(logging.Formatter):

    def format(self, record):
        log_record = {
            "time": time.strftime("%H - %M - %S"),
            "level": record.levelname,
            "logger": record.name,
            "line number": record.lineno,
            "message": record.getMessage()
        }

        if record.args and isinstance(record.args, dict):
            log_record.update(record.args)

        return json.dumps(log_record, ensure_ascii=False)


dict_logger = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": JsonFormatter
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "level": "INFO"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "json",
            "filename": "logs/app.log",
            "level": "DEBUG"
        }
    },
    "loggers": {
        "app_logger": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False
        }
    }
}
