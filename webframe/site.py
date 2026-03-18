"""Render external websites in Jupyter using IFrame."""

from IPython.display import IFrame, display

from webframe.validators import validate_url, validate_https
from webframe.logger import get_logger
from webframe.exceptions import InvalidURLError

logger = get_logger(__name__)


def render_site(url, width=900, height=500, enforce_https=True):
    """Render a website in a Jupyter notebook cell.

    Args:
        url: Website URL to display
        width: iframe width (default 900)
        height: iframe height (default 500)
        enforce_https: Force HTTPS only (default True)
    """
    logger.info(f"Attempting to render website: {url}")

    # Validate URL format
    if not validate_url(url):
        logger.error(f"Invalid URL format: {url}")
        raise InvalidURLError(f"Invalid URL format: {url}. Please provide a valid URL.")

    # Validate HTTPS if enforced
    if enforce_https and not validate_https(url):
        logger.error(f"URL must use HTTPS: {url}")
        raise InvalidURLError(
            f"URL must use HTTPS: {url}. "
            "Use enforce_https=False to allow HTTP."
        )

    # Validate dimensions
    if width <= 0 or height <= 0:
        logger.error(f"Invalid dimensions: width={width}, height={height}")
        raise ValueError("Width and height must be positive integers")

    logger.info(f"Successfully rendering: {url} ({width}x{height})")

    # Create and return IFrame
    iframe = IFrame(src=url, width=width, height=height)
    display(iframe)
    return iframe
