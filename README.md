# kartik-webframe

[![Tests](https://github.com/KartikSuryavanshi/Webframe-Package/actions/workflows/tests.yml/badge.svg)](https://github.com/KartikSuryavanshi/Webframe-Package/actions/workflows/tests.yml)
[![PyPI version](https://badge.fury.io/py/kartik-webframe.svg)](https://badge.fury.io/py/kartik-webframe)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple Python library to embed websites and YouTube videos in Jupyter notebooks.

**📦 PyPI:** https://pypi.org/project/kartik-webframe/

## What's New (v0.2.0)

- PDF and Google Doc embedding: `render_pdf(url)`
- Grid layout for multiple embeds: `render_grid(urls, ncols=2)`
- 100% test coverage, improved error handling, and more natural code style

## Why?

When working in Jupyter notebooks, I got tired of switching between browser tabs to check documentation or watch tutorials. This library lets you view websites and videos right inside your notebook cells.

## Installation

```bash
pip install kartik-webframe
```

Or install from source:

```bash
git clone https://github.com/KartikSuryavanshi/Webframe-Package.git
cd Webframe-Package
pip install -e .
```

## Usage

### Quick Start

```python
# Install the package
# pip install kartik-webframe

# Import and use
from webframe import render_site, render_youtube_video

# Render a website
render_site("https://docs.python.org")

# Render a YouTube video
render_youtube_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
```

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

### Embed PDFs and Google Docs

```python
from webframe import render_pdf

render_pdf("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")
render_pdf("https://docs.google.com/document/d/1A2B3C4D5E6F7G8H9I0J/edit")
```

### Embed Multiple Items in a Grid

```python
from webframe import render_grid

render_grid([
    "https://docs.python.org/3/",
    "https://www.wikipedia.org/",
    "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
], ncols=2)
```

## How It Works

Uses IPython's display functionality to render IFrames for websites and HTML embeds for YouTube videos. Only works in Jupyter notebooks or Google Colab.

## Requirements

- Python 3.7+
- IPython ≥ 7.0.0

## Development

### Running Tests

```bash
pytest
```

### Building Package

```bash
python -m build
```

## License

MIT - Copyright (c) 2026 Kartik Suryavanshi

---

**Made with ❤️**
