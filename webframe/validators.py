"""URL validation helpers."""

import re
from urllib.parse import urlparse, parse_qs


def validate_url(url):
    """Check if string is a valid URL."""
    if not url or not isinstance(url, str):
        return False

    result = urlparse(url)
    return bool(result.scheme and result.netloc)


def validate_https(url):
    """Check if URL uses HTTPS."""
    if not validate_url(url):
        return False

    result = urlparse(url)
    return result.scheme == "https"


def extract_youtube_id(url):
    """Extract video ID from various YouTube URL formats."""
    if not url or not isinstance(url, str):
        return None

    # Standard watch URL pattern
    pattern1 = r'(?:youtube\.com\/watch\?v=)([\w-]+)'
    match = re.search(pattern1, url)
    if match:
        return match.group(1)

    # Short URL
    pattern2 = r'(?:youtu\.be\/)([\w-]+)'
    match = re.search(pattern2, url)
    if match:
        return match.group(1)

    # Embed URL
    pattern3 = r'(?:youtube\.com\/embed\/)([\w-]+)'
    match = re.search(pattern3, url)
    if match:
        return match.group(1)

    # Fallback: parse query parameters
    parsed = urlparse(url)
    if 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc:
        if parsed.query:
            params = parse_qs(parsed.query)
            if 'v' in params:
                return params['v'][0]
        if parsed.path:
            path_parts = parsed.path.strip('/').split('/')
            if path_parts and len(path_parts[0]) == 11:
                return path_parts[0]

    return None
