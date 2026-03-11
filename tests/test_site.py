"""
Unit tests for the site rendering module.

Tests cover URL validation, HTTPS enforcement, dimension validation,
and IFrame rendering functionality.
"""

import pytest
from unittest.mock import patch, MagicMock
from IPython.display import IFrame

from webframe.site import render_site
from webframe.exceptions import InvalidURLError


class TestRenderSite:
    """Test cases for render_site function."""

    @patch('webframe.site.display')
    def test_render_site_valid_https_url(self, mock_display):
        """Test rendering a valid HTTPS URL."""
        url = "https://docs.python.org"
        result = render_site(url)

        assert isinstance(result, IFrame)
        assert result.src == url
        assert result.width == 900  # default width
        assert result.height == 500  # default height
        mock_display.assert_called_once()

    @patch('webframe.site.display')
    def test_render_site_custom_dimensions(self, mock_display):
        """Test rendering with custom width and height."""
        url = "https://example.com"
        width = 1200
        height = 800
        result = render_site(url, width=width, height=height)

        assert isinstance(result, IFrame)
        assert result.width == width
        assert result.height == height
        mock_display.assert_called_once()

    @patch('webframe.site.display')
    def test_render_site_http_url_with_enforcement(self, mock_display):
        """Test that HTTP URLs are rejected when HTTPS is enforced."""
        url = "http://example.com"

        with pytest.raises(InvalidURLError) as exc_info:
            render_site(url, enforce_https=True)

        assert "must use HTTPS" in str(exc_info.value)
        mock_display.assert_not_called()

    @patch('webframe.site.display')
    def test_render_site_http_url_without_enforcement(self, mock_display):
        """Test that HTTP URLs are allowed when HTTPS is not enforced."""
        url = "http://example.com"
        result = render_site(url, enforce_https=False)

        assert isinstance(result, IFrame)
        assert result.src == url
        mock_display.assert_called_once()

    @patch('webframe.site.display')
    def test_render_site_invalid_url(self, mock_display):
        """Test that invalid URLs raise an error."""
        url = "not a valid url"

        with pytest.raises(InvalidURLError) as exc_info:
            render_site(url)

        assert "Invalid URL format" in str(exc_info.value)
        mock_display.assert_not_called()

    @patch('webframe.site.display')
    def test_render_site_invalid_dimensions(self, mock_display):
        """Test that invalid dimensions raise an error."""
        url = "https://example.com"

        with pytest.raises(ValueError):
            render_site(url, width=-100, height=500)

        with pytest.raises(ValueError):
            render_site(url, width=900, height=0)

        mock_display.assert_not_called()

    @patch('webframe.site.display')
    def test_render_site_empty_url(self, mock_display):
        """Test that empty URLs are rejected."""
        url = ""

        with pytest.raises(InvalidURLError):
            render_site(url)

        mock_display.assert_not_called()
