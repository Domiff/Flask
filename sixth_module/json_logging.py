import logging.config

from sixth_module.dict_config import dict_logger

logging.config.dictConfig(dict_logger)
logger = logging.getLogger("app_logger")

logger.info("hello")
logger.debug("'")
