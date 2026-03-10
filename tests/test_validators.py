"""
Unit tests for the validators module.
"""

import pytest
from webframe.validators import (
    validate_url,
    validate_https,
    extract_youtube_id
)


class TestValidateURL:
    """Test cases for validate_url function."""

    def test_valid_https_url(self):
        """Test validation of valid HTTPS URLs."""
        assert validate_url("https://example.com") is True
        assert validate_url("https://www.google.com") is True
        assert validate_url("https://docs.python.org/3/") is True

    def test_valid_http_url(self):
        """Test validation of valid HTTP URLs."""
        assert validate_url("http://example.com") is True
        assert validate_url("http://localhost:8000") is True

    def test_invalid_url(self):
        """Test validation of invalid URLs."""
        assert validate_url("not a url") is False
        assert validate_url("just-text") is False
        assert validate_url("") is False
        assert validate_url("   ") is False

    def test_none_or_non_string(self):
        """Test validation with None or non-string inputs."""
        assert validate_url(None) is False
        assert validate_url(123) is False
        assert validate_url([]) is False


class TestValidateHTTPS:
    """Test cases for validate_https function."""

    def test_https_url(self):
        """Test validation of HTTPS URLs."""
        assert validate_https("https://example.com") is True
        assert validate_https("https://www.google.com") is True

    def test_http_url(self):
        """Test validation of HTTP URLs (should fail)."""
        assert validate_https("http://example.com") is False
        assert validate_https("http://localhost:8000") is False

    def test_invalid_url(self):
        """Test validation of invalid URLs."""
        assert validate_https("not a url") is False
        assert validate_https("") is False

    def test_ftp_url(self):
        """Test validation of non-HTTP protocols."""
        assert validate_https("ftp://example.com") is False


class TestExtractYouTubeID:
    """Test cases for extract_youtube_id function."""

    def test_standard_watch_url(self):
        """Test extraction from standard youtube.com/watch URLs."""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        assert extract_youtube_id(url) == "dQw4w9WgXcQ"

    def test_short_url(self):
        """Test extraction from youtu.be short URLs."""
        url = "https://youtu.be/dQw4w9WgXcQ"
        assert extract_youtube_id(url) == "dQw4w9WgXcQ"

    def test_embed_url(self):
        """Test extraction from youtube.com/embed URLs."""
        url = "https://www.youtube.com/embed/dQw4w9WgXcQ"
        assert extract_youtube_id(url) == "dQw4w9WgXcQ"

    def test_mobile_url(self):
        """Test extraction from mobile YouTube URLs."""
        url = "https://m.youtube.com/watch?v=dQw4w9WgXcQ"
        assert extract_youtube_id(url) == "dQw4w9WgXcQ"

    def test_url_with_additional_params(self):
        """Test extraction from URLs with additional query parameters."""
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=42s"
        assert extract_youtube_id(url) == "dQw4w9WgXcQ"

    def test_url_without_www(self):
        """Test extraction from URLs without www."""
        url = "https://youtube.com/watch?v=dQw4w9WgXcQ"
        assert extract_youtube_id(url) == "dQw4w9WgXcQ"

    def test_invalid_url(self):
        """Test extraction from invalid URLs."""
        assert extract_youtube_id("https://example.com") is None
        assert extract_youtube_id("not a url") is None
        assert extract_youtube_id("") is None

    def test_none_or_non_string(self):
        """Test extraction with None or non-string inputs."""
        assert extract_youtube_id(None) is None
        assert extract_youtube_id(123) is None
        assert extract_youtube_id([]) is None

    def test_youtube_url_without_video_id(self):
        """Test extraction from YouTube URLs without video ID."""
        assert extract_youtube_id("https://www.youtube.com") is None
        assert extract_youtube_id("https://www.youtube.com/") is None

    def test_various_video_ids(self):
        """Test extraction of various video ID formats."""
        # Test different video IDs
        test_ids = [
            "dQw4w9WgXcQ",
            "rfscVS0vtbw",
            "9bZkp7q19f0",
            "abc-DEF_123"
        ]

        for video_id in test_ids:
            url = f"https://www.youtube.com/watch?v={video_id}"
            assert extract_youtube_id(url) == video_id
