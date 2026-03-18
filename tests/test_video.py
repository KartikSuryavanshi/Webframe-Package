"""Tests for YouTube video rendering."""

import pytest
from unittest.mock import patch
from IPython.display import HTML

from webframe.video import render_youtube_video
from webframe.exceptions import InvalidYouTubeURLError


class TestRenderYouTubeVideo:

    @patch('webframe.video.display')
    def test_render_youtube_video_standard_url(self, mock_display):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        result = render_youtube_video(url)

        assert isinstance(result, HTML)
        assert "dQw4w9WgXcQ" in result.data
        assert "youtube.com/embed/dQw4w9WgXcQ" in result.data
        mock_display.assert_called_once()

    @patch('webframe.video.display')
    def test_render_youtube_video_short_url(self, mock_display):
        url = "https://youtu.be/dQw4w9WgXcQ"
        result = render_youtube_video(url)

        assert isinstance(result, HTML)
        assert "dQw4w9WgXcQ" in result.data
        mock_display.assert_called_once()

    @patch('webframe.video.display')
    def test_render_youtube_video_custom_dimensions(self, mock_display):
        url = "https://www.youtube.com/watch?v=rfscVS0vtbw"
        width = 1000
        height = 600
        result = render_youtube_video(url, width=width, height=height)

        assert isinstance(result, HTML)
        assert f'width="{width}"' in result.data
        assert f'height="{height}"' in result.data
        mock_display.assert_called_once()

    @patch('webframe.video.display')
    def test_render_youtube_video_with_autoplay(self, mock_display):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        result = render_youtube_video(url, autoplay=True)

        assert isinstance(result, HTML)
        assert "autoplay=1" in result.data
        mock_display.assert_called_once()

    @patch('webframe.video.display')
    def test_render_youtube_video_with_mute(self, mock_display):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        result = render_youtube_video(url, mute=True)

        assert isinstance(result, HTML)
        assert "mute=1" in result.data
        mock_display.assert_called_once()

    @patch('webframe.video.display')
    def test_render_youtube_video_with_autoplay_and_mute(self, mock_display):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        result = render_youtube_video(url, autoplay=True, mute=True)

        assert isinstance(result, HTML)
        assert "autoplay=1" in result.data
        assert "mute=1" in result.data
        mock_display.assert_called_once()

    @patch('webframe.video.display')
    def test_render_youtube_video_invalid_url(self, mock_display):
        url = "https://example.com/not-youtube"

        with pytest.raises(InvalidYouTubeURLError) as exc_info:
            render_youtube_video(url)

        assert "Invalid YouTube URL" in str(exc_info.value)
        mock_display.assert_not_called()

    @patch('webframe.video.display')
    def test_render_youtube_video_invalid_dimensions(self, mock_display):
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

        with pytest.raises(ValueError):
            render_youtube_video(url, width=-100, height=450)

        with pytest.raises(ValueError):
            render_youtube_video(url, width=800, height=0)

        mock_display.assert_not_called()

    @patch('webframe.video.display')
    def test_render_youtube_video_empty_url(self, mock_display):
        url = ""

        with pytest.raises(InvalidYouTubeURLError):
            render_youtube_video(url)

        mock_display.assert_not_called()

    @patch('webframe.video.display')
    def test_render_youtube_video_embed_url(self, mock_display):
        url = "https://www.youtube.com/embed/dQw4w9WgXcQ"
        result = render_youtube_video(url)

        assert isinstance(result, HTML)
        assert "dQw4w9WgXcQ" in result.data
        mock_display.assert_called_once()
