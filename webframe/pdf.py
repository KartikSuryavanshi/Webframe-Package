"""PDF and document embedding for Jupyter notebooks."""

from IPython.display import IFrame, display, HTML
from webframe.logger import get_logger
from webframe.validators import validate_url

logger = get_logger(__name__)


def render_pdf(url, width=900, height=600):
    """Embed a PDF or Google Doc in a Jupyter notebook cell.

    Args:
        url: The URL to the PDF or Google Doc
        width: Width of the iframe (default 900)
        height: Height of the iframe (default 600)
    """
    logger.info(f"Attempting to render PDF/document: {url}")
    if not validate_url(url):
        logger.error(f"Invalid URL format: {url}")
        display(HTML(f'<div style="color:red;">Invalid URL: {url}</div>'))
        return None

    # Google Docs viewer for PDFs not directly embeddable
    if url.lower().endswith('.pdf'):
        iframe_url = f"https://docs.google.com/gview?url={url}&embedded=true"
    elif 'docs.google.com' in url:
        iframe_url = url
    else:
        # Try direct embedding
        iframe_url = url

    iframe = IFrame(src=iframe_url, width=width, height=height)
    display(iframe)
    return iframe
