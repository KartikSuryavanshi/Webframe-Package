"""
Video rendering module for WebFrame.

This module provides functionality to embed YouTube videos
inside Jupyter Notebook cells using HTML iframe.
"""

from typing import Optional
from IPython.display import HTML, display

from webframe.validators import extract_youtube_id
from webframe.logger import get_logger
from webframe.exceptions import InvalidYouTubeURLError

logger = get_logger(__name__)


def render_youtube_video(
    url: str,
    width: int = 800,
    height: int = 450,
    autoplay: bool = False,
    mute: bool = False
) -> HTML:
    """
    Render a YouTube video inside a Jupyter Notebook cell.

    Args:
        url: The YouTube video URL
        width: Width of the video player in pixels (default: 800)
        height: Height of the video player in pixels (default: 450)
        autoplay: Whether to autoplay the video (default: False)
        mute: Whether to mute the video (default: False)

    Returns:
        HTML: An IPython HTML object containing the embedded video

    Raises:
        InvalidYouTubeURLError: If the YouTube URL is invalid

    Example:
        >>> from webframe import render_youtube_video
        >>> render_youtube_video("https://www.youtube.com/watch?v=rfscVS0vtbw")
    """
    logger.info(f"Attempting to render YouTube video: {url}")

    # Extract video ID from URL
    video_id = extract_youtube_id(url)
    if not video_id:
        logger.error(f"Invalid YouTube URL: {url}")
        raise InvalidYouTubeURLError(f"Invalid YouTube URL: {url}")

    # Validate dimensions
    if width <= 0 or height <= 0:
        logger.error(f"Invalid dimensions: width={width}, height={height}")
        raise ValueError("Width and height must be positive integers")

    # Build embed URL with parameters
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    params = []

    if autoplay:
        params.append("autoplay=1")
    if mute:
        params.append("mute=1")

    if params:
        embed_url += "?" + "&".join(params)

    logger.info(f"Successfully rendering video: {video_id} ({width}x{height})")

    # Create iframe HTML
    iframe_html = f"""
    <iframe
        width="{width}"
        height="{height}"
        src="{embed_url}"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
    """

    # Create and return HTML object
    html_obj = HTML(iframe_html)
    display(html_obj)
    return html_obj
