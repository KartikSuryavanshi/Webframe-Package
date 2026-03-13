# WebFrame

A simple Python library to embed websites and YouTube videos in Jupyter notebooks.

## Why?

When working in Jupyter notebooks, I got tired of switching between browser tabs to check documentation or watch tutorials. This library lets you view websites and videos right inside your notebook cells.

## Installation

```bash
pip install -e .
```

## Usage

### Embed a Website

```python
from webframe import render_site

render_site("https://docs.python.org")
render_site("https://github.com", width=1200, height=800)

```

### Embed YouTube Videos

```python
from webframe import render_youtube_video

render_youtube_video("https://www.youtube.com/watch?v=VIDEO_ID")

# Short URLs work too
render_youtube_video("https://youtu.be/VIDEO_ID")

# Custom size and autoplay
render_youtube_video("https://youtu.be/VIDEO_ID", width=1000, height=600, autoplay=True, mute=True)
```

## How It Works

Uses IPython's display functionality to render IFrames for websites and HTML embeds for YouTube videos. Only works in Jupyter notebooks or Google Colab.

## Requirements

- Python 3.7+
- IPython

## Testing

```bash
pytest
```

## License

MIT
