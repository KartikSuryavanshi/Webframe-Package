"""Tests for PDF/document embedding."""

from webframe.pdf import render_pdf
from IPython.display import IFrame
from unittest.mock import patch

    
class TestRenderPDF:
    @patch('webframe.pdf.display')
    def test_render_pdf_valid_url(self, mock_display):
        url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        result = render_pdf(url)
        assert isinstance(result, IFrame)
        assert "docs.google.com/gview" in result.src
        mock_display.assert_called_once()

    @patch('webframe.pdf.display')
    def test_render_pdf_invalid_url(self, mock_display):
        url = "not a url"
        result = render_pdf(url)
        assert result is None
        mock_display.assert_called_once()

    @patch('webframe.pdf.display')
    def test_render_pdf_google_doc(self, mock_display):
        url = "https://docs.google.com/document/d/1A2B3C4D5E6F7G8H9I0J/edit"
        result = render_pdf(url)
        assert isinstance(result, IFrame)
        assert url in result.src
        mock_display.assert_called_once()
