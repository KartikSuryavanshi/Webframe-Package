"""YouTube video embedding for Jupyter notebooks."""

from IPython.display import HTML, display

from webframe.validators import extract_youtube_id
from webframe.logger import get_logger
from webframe.exceptions import InvalidYouTubeURLError

logger = get_logger(__name__)


def render_youtube_video(url, width=800, height=450,
                         autoplay=False, mute=False):
    """Embed a YouTube video in Jupyter.

    Supports youtube.com/watch, youtu.be, and embed URLs.
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

    # TODO: maybe add support for start time parameter (t=30s)
    # Create iframe HTML
    iframe_html = f"""
    <iframe
        width="{width}"
        height="{height}"
        src="{embed_url}"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write;
               encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
    """

    # Create and return HTML object
    html_obj = HTML(iframe_html)
    display(html_obj)
    return html_obj
