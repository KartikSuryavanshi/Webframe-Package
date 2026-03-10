"""
Custom exceptions for WebFrame package.
"""


class WebFrameError(Exception):
    """Base exception class for WebFrame package."""
    pass


class InvalidURLError(WebFrameError):
    """Raised when a URL is invalid or doesn't meet requirements."""
    pass


class InvalidYouTubeURLError(WebFrameError):
    """Raised when a YouTube URL is invalid or cannot be parsed."""
    pass


class RenderError(WebFrameError):
    """Raised when rendering fails for any reason."""
    pass
