import json
import logging


class JsonAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):
        return json.dumps(msg), kwargs


logging.basicConfig(level=logging.INFO,
                    filename="logs/log.log",
                    format="%(asctime)s - %(module)s - %(message)s"
                    )

logger = logging.getLogger("app_logger")

user_loger = JsonAdapter(logger)

user_loger.info("")