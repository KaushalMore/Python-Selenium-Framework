import logging
import os
from logging.handlers import RotatingFileHandler

# logs package log
def get_logger(name):
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)
    os.makedirs("logs", exist_ok=True)

    console_handler = logging.StreamHandler()
    file_handler = RotatingFileHandler("logs/test_log.log", maxBytes=3000000, backupCount=3)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# import logging
# import os
#
# # report package log
# def get_logger(name):
#     logger = logging.getLogger(name)
#
#     if logger.hasHandlers():
#         logger.handlers.clear()
#
#     logger.setLevel(logging.INFO)
#     log_dir = os.path.join(
#         os.path.dirname(os.path.dirname(__file__)),
#         "reports",
#         "logs"
#     )
#
#     os.makedirs(log_dir, exist_ok=True)
#
#     log_file = os.path.join(log_dir, "test.log")
#     file_handler = logging.FileHandler(log_file)
#     console_handler = logging.StreamHandler()
#
#     formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#
#     file_handler.setFormatter(formatter)
#     console_handler.setFormatter(formatter)
#
#     logger.addHandler(file_handler)
#     logger.addHandler(console_handler)
#
#     return logger
