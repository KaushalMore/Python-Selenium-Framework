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


# combination of both, in reports package logs, it creates new log file for every test and logs package is appended.
# import logging
# import os
# from logging.handlers import RotatingFileHandler
#
# def get_logger(name: str, request=None):
#     logger = logging.getLogger(name)
#
#     # Clear existing handlers to avoid duplicates
#     if logger.hasHandlers():
#         logger.handlers.clear()
#
#     logger.setLevel(logging.INFO)
#
#     # --- Persistent suite log (append + rotate) ---
#     logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
#     os.makedirs(logs_dir, exist_ok=True)
#     suite_log_file = os.path.join(logs_dir, "test_log.log")
#
#     rotating_handler = RotatingFileHandler(
#         suite_log_file, maxBytes=3_000_000, backupCount=3
#     )
#     rotating_formatter = logging.Formatter(
#         "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#     )
#     rotating_handler.setFormatter(rotating_formatter)
#
#     # --- Per-test log (overwrite each test run) ---
#     reports_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports", "logs")
#     os.makedirs(reports_dir, exist_ok=True)
#
#     if request:
#         class_name = request.node.cls.__name__ if request.node.cls else "NoClass"
#         test_name = request.node.name
#         test_log_file = os.path.join(reports_dir, f"{class_name}_{test_name}.log")
#     else:
#         test_log_file = os.path.join(reports_dir, "test.log")
#
#     test_handler = logging.FileHandler(test_log_file, mode="w")
#     test_formatter = logging.Formatter(
#         "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#     )
#     test_handler.setFormatter(test_formatter)
#
#     # --- Console handler ---
#     console_handler = logging.StreamHandler()
#     console_handler.setFormatter(rotating_formatter)
#
#     # Attach all handlers
#     logger.addHandler(rotating_handler)  # persistent suite log
#     logger.addHandler(test_handler)      # per-test log
#     logger.addHandler(console_handler)   # console output
#
#     return logger
