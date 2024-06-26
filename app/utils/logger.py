import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_information(msg : str):
    logger.info(msg)
def log_error(msg :str):
    logger.error(msg)