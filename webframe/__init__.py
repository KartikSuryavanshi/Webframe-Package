"""
WebFrame - Render websites and videos in Jupyter notebooks.

Simple library to embed external websites and YouTube videos
directly in Jupyter or Colab cells.
"""

from webframe.site import render_site
from webframe.video import render_youtube_video

__version__ = "0.1.0"
__author__ = "Kartik Suryavanshi"
__all__ = ["render_site", "render_youtube_video"]
