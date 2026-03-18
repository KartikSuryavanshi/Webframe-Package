"""Simple logging setup."""

import logging
import sys


def get_logger(name, level=logging.INFO, format_string=None):
    """Get a configured logger."""
    logger = logging.getLogger(name)

    # Avoid adding handlers multiple times if logger already configured
    if logger.handlers:
        return logger

    logger.setLevel(level)

    # Create console handler with specified level
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    # Set format
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    formatter = logging.Formatter(format_string)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


# Default package logger
default_logger = get_logger("webframe")
