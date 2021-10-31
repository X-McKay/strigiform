"""Logging utility."""
import logging


def logger_init(name: str, level: int = logging.INFO):
    """Initializes logger.

    :param name: Class name
    :type name: str
    :param level: Level of logging, defaults to logging.INFO
    :type level: int, optional
    """
    format = f"%(asctime)s - %(filename)s: Line %(lineno)s - %(funcName)s(): %(message)s"  # noqa: F541
    logging.root.handlers = []
    logging.basicConfig(format=format, level=level)
    return logging.getLogger(name=name)
