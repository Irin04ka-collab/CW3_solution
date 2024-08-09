import logging

from config import PATH_LOG

def create_logger():
    logger = logging.getLogger("basic")
    loger_api = logging.getLogger("api")
    loger_api.setLevel("INFO")
    logger.setLevel('WARNING')

    file_handler = logging.FileHandler('logs/logger.log')
    file_handler_api = logging.FileHandler('logs/api.log')

    formatter = logging.Formatter("%(levelname)s %(asctime)s: %(message)s >> %(funcName)s")

    file_handler.setFormatter(formatter)
    file_handler_api.setFormatter(formatter)

    logger.addHandler(file_handler)
    loger_api.addHandler(file_handler_api)

    return logger
