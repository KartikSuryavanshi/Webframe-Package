"""Tests for grid layout embedding."""
from webframe.grid import render_grid
from unittest.mock import patch


class TestRenderGrid:
    @patch('webframe.grid.display')
    def test_render_grid_valid_urls(self, mock_display):
        urls = [
            "https://docs.python.org/3/",
            "https://www.wikipedia.org/",
            "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        ]
        render_grid(urls, width=200, height=150, ncols=2)
        assert mock_display.called
        html = mock_display.call_args[0][0].data
        assert "iframe" in html
        assert html.count("<iframe") == 3
        assert html.count("<tr>") >= 1

    @patch('webframe.grid.display')
    def test_render_grid_invalid_url(self, mock_display):
        urls = ["not a url", "https://docs.python.org/3/"]
        render_grid(urls, ncols=1)
        html = mock_display.call_args[0][0].data
        assert "Invalid URL" in html
        assert "iframe" in html

    @patch('webframe.grid.display')
    def test_render_grid_empty(self, mock_display):
        render_grid([], ncols=2)
        html = mock_display.call_args[0][0].data
        assert "table" in html
