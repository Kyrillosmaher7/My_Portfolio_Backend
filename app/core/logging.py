import logging
import os
from datetime import datetime

LOG_DIR = "app/logs"
os.makedirs(LOG_DIR, exist_ok=True)


def get_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # 1. CONSOLE (INFO + above)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # 2. FILE (WARNING + ERROR)
    today = datetime.now().strftime("%Y-%m-%d")
    file_handler = logging.FileHandler(f"{LOG_DIR}/{today}.log")

    file_handler.setLevel(logging.WARNING)  # 🔥 KEY CHANGE
    file_handler.setFormatter(formatter)

    # attach handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger