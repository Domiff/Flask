import logging
from time import strftime


time = strftime("%H-%M-%S")
formatter = "%(name)s - %(levelname)s - %(asctime)s - %(message)s"

logging.basicConfig(filename="logs/stderr.txt",
                    level=logging.INFO,
                    format=formatter,
                    datefmt=time, style="%")

logger = logging.getLogger("Name")




logger.info("Hello")