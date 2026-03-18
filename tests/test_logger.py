"""Tests for logging module."""

import logging
from webframe.logger import get_logger


class TestGetLogger:

    def test_basic_logger_creation(self):
        logger = get_logger("test_logger")
        assert logger is not None
        assert logger.name == "test_logger"
        assert logger.level == logging.INFO

    def test_logger_with_custom_level(self):
        logger = get_logger("test_custom", level=logging.DEBUG)
        assert logger.level == logging.DEBUG

    def test_logger_already_configured(self):
        # First call creates logger with handler
        logger1 = get_logger("test_reuse")
        handler_count = len(logger1.handlers)

        # Second call should return same logger without adding new handlers
        logger2 = get_logger("test_reuse")
        assert logger1 is logger2
        assert len(logger2.handlers) == handler_count

    def test_custom_format_string(self):
        custom_format = "%(levelname)s - %(message)s"
        logger = get_logger("test_format", format_string=custom_format)
        assert len(logger.handlers) > 0
