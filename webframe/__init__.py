"""
WebFrame - Render websites and videos inside Jupyter notebooks.

A production-ready Python library that allows users to render external websites
and YouTube videos directly inside Jupyter Notebook or Google Colab cells.

Usage:
    from webframe import render_site, render_youtube_video
    
    render_site("https://docs.python.org")
    render_youtube_video("https://www.youtube.com/watch?v=VIDEO_ID")
"""

from webframe.site import render_site
from webframe.video import render_youtube_video

__version__ = "0.1.0"
__author__ = "WebFrame Contributors"
__all__ = ["render_site", "render_youtube_video"]
