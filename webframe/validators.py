"""
URL validation utilities for WebFrame package.
"""

import re
from typing import Optional
from urllib.parse import urlparse, parse_qs


def validate_url(url: str) -> bool:
    """
    Validate if a string is a properly formatted URL.

    Args:
        url: The URL string to validate

    Returns:
        bool: True if the URL is valid, False otherwise

    Example:
        >>> validate_url("https://example.com")
        True
        >>> validate_url("not a url")
        False
    """
    if not url or not isinstance(url, str):
        return False

    try:
        # Parse URL and check for required components (scheme and netloc)
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def validate_https(url: str) -> bool:
    """
    Validate if a URL uses HTTPS protocol.

    Args:
        url: The URL string to validate

    Returns:
        bool: True if the URL uses HTTPS, False otherwise

    Example:
        >>> validate_https("https://example.com")
        True
        >>> validate_https("http://example.com")
        False
    """
    if not validate_url(url):
        return False

    try:
        result = urlparse(url)
        return result.scheme == "https"
    except Exception:
        return False


def extract_youtube_id(url: str) -> Optional[str]:
    """
    Extract the video ID from a YouTube URL.

    Supports various YouTube URL formats:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    - https://m.youtube.com/watch?v=VIDEO_ID

    Args:
        url: The YouTube URL to parse

    Returns:
        Optional[str]: The video ID if found, None otherwise

    Example:
        >>> extract_youtube_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        'dQw4w9WgXcQ'
        >>> extract_youtube_id("https://youtu.be/dQw4w9WgXcQ")
        'dQw4w9WgXcQ'
    """
    if not url or not isinstance(url, str):
        return None

    # Pattern 1: youtube.com/watch?v=VIDEO_ID
    # Matches standard YouTube watch URLs
    pattern1 = r'(?:youtube\.com\/watch\?v=)([\w-]+)'
    match = re.search(pattern1, url)
    if match:
        return match.group(1)

    # Pattern 2: youtu.be/VIDEO_ID
    pattern2 = r'(?:youtu\.be\/)([\w-]+)'
    match = re.search(pattern2, url)
    if match:
        return match.group(1)

    # Pattern 3: youtube.com/embed/VIDEO_ID
    pattern3 = r'(?:youtube\.com\/embed\/)([\w-]+)'
    match = re.search(pattern3, url)
    if match:
        return match.group(1)

    # Pattern 4: Using urlparse for query parameters
    try:
        parsed = urlparse(url)
        if 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc:
            # Check if it's in query parameters
            if parsed.query:
                params = parse_qs(parsed.query)
                if 'v' in params:
                    return params['v'][0]
            # Check if it's in the path (for youtu.be format)
            if parsed.path:
                path_parts = parsed.path.strip('/').split('/')
                if path_parts and len(path_parts[0]) == 11:  # YouTube IDs are 11 chars
                    return path_parts[0]
    except Exception:
        pass

    return None
