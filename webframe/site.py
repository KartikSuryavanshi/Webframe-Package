"""
Site rendering module for WebFrame.

This module provides functionality to render external websites
inside Jupyter Notebook cells using IFrame.
"""

from typing import Optional
from IPython.display import IFrame, display

from webframe.validators import validate_url, validate_https
from webframe.logger import get_logger
from webframe.exceptions import InvalidURLError

logger = get_logger(__name__)


def render_site(
    url: str,
    width: int = 900,
    height: int = 500,
    enforce_https: bool = True
) -> IFrame:
    """
    Render an external website inside a Jupyter Notebook cell.

    Args:
        url: The URL of the website to render
        width: Width of the iframe in pixels (default: 900)
        height: Height of the iframe in pixels (default: 500)
        enforce_https: Whether to enforce HTTPS URLs (default: True)

    Returns:
        IFrame: An IPython IFrame object containing the rendered website

    Raises:
        InvalidURLError: If the URL is invalid or doesn't meet requirements

    Example:
        >>> from webframe import render_site
        >>> render_site("https://docs.python.org")
    """
    logger.info(f"Attempting to render website: {url}")

    # Validate URL format
    if not validate_url(url):
        logger.error(f"Invalid URL format: {url}")
        raise InvalidURLError(f"Invalid URL format: {url}. Please provide a valid URL.")

    # Validate HTTPS if enforced
    if enforce_https and not validate_https(url):
        logger.error(f"URL must use HTTPS: {url}")
        raise InvalidURLError(f"URL must use HTTPS: {url}. Use enforce_https=False to allow HTTP.")

    # Validate dimensions
    if width <= 0 or height <= 0:
        logger.error(f"Invalid dimensions: width={width}, height={height}")
        raise ValueError("Width and height must be positive integers")

    logger.info(f"Successfully rendering: {url} ({width}x{height})")

    # Create and return IFrame
    iframe = IFrame(src=url, width=width, height=height)
    display(iframe)
    return iframe
