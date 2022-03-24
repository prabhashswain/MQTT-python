import logging
import time

logging.basicConfig(
    format="%(asctime)s:%(levelname)s:%(message)s",level=logging.DEBUG
)

def log(level,msg):
    match level:
        case "DEBUG":
            logging.debug(str(msg))
        case "ERROR":
            logging.error(str(msg))
        case _:
            logging.info(str(msg))