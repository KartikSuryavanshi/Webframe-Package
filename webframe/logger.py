"""
Logging configuration for WebFrame package.
"""

import logging
import sys
from typing import Optional


def get_logger(
    name: str,
    level: int = logging.INFO,
    format_string: Optional[str] = None
) -> logging.Logger:
    """
    Get a configured logger instance.

    Args:
        name: Name of the logger (typically __name__ from calling module)
        level: Logging level (default: logging.INFO)
        format_string: Custom format string for log messages

    Returns:
        logging.Logger: Configured logger instance

    Example:
        >>> logger = get_logger(__name__)
        >>> logger.info("This is an info message")
    """
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
