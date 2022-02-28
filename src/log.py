import logging
from logging import handlers


def get_logger(mod_name: str):
    logger = logging.getLogger(mod_name)
    handler = handlers.RotatingFileHandler(filename="./logs/app.log", mode="a", maxBytes=102400, backupCount=1)
    formatter = logging.Formatter(
        "%(asctime)s : %(filename)s : %(funcName)s : %(levelname)s : %(message)s", datefmt="%d-%b-%y %H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
