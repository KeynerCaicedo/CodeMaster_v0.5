import logging
from logging.handlers import RotatingFileHandler
import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

def get_logger(name: str):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(LOG_LEVEL)
    ch = RotatingFileHandler('backend.log', maxBytes=10_000_000, backupCount=3)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
    return logger
