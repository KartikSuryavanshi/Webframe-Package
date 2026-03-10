# WebFrame 🌐

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**WebFrame** is a production-ready Python library that allows you to render external websites and YouTube videos directly inside Jupyter Notebook or Google Colab cells, without leaving your coding environment.

## ✨ Features

- 🌐 **Website Embedding**: Render any website directly in notebook cells using IFrame
- 🎥 **YouTube Integration**: Embed YouTube videos with customizable players
- 🔒 **Security**: Built-in HTTPS enforcement and URL validation
- 🎨 **Customizable**: Adjust dimensions, autoplay, mute, and more
- 🧪 **Well-Tested**: Comprehensive test suite with pytest
- 📝 **Type-Hinted**: Full type hints for better IDE support
- 🛠️ **Production-Ready**: Proper logging, error handling, and code quality tools

## 📦 Installation

### From PyPI (when published)

```bash
pip install webframe
```

### For Development

```bash
# Clone the repository
git clone https://github.com/yourusername/webframe.git
cd webframe

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

## 🚀 Quick Start

### Rendering Websites

```python
from webframe import render_site

# Render a website with default dimensions (900x500)
render_site("https://docs.python.org")

# Customize dimensions
render_site("https://github.com", width=1200, height=800)

# Allow HTTP URLs (HTTPS enforced by default)
render_site("http://example.com", enforce_https=False)
```

### Embedding YouTube Videos

```python
from webframe import render_youtube_video

# Standard YouTube URL
render_youtube_video("https://www.youtube.com/watch?v=rfscVS0vtbw")

# Short URL format
render_youtube_video("https://youtu.be/dQw4w9WgXcQ")

# With custom dimensions
render_youtube_video(
    "https://www.youtube.com/watch?v=rfscVS0vtbw",
    width=1000,
    height=600
)

# With autoplay and mute
render_youtube_video(
    "https://youtu.be/dQw4w9WgXcQ",
    autoplay=True,
    mute=True
)
```

## 📚 Complete Example

```python
# Example Jupyter Notebook

from webframe import render_site, render_youtube_video

# 1. Embed Python documentation
print("📖 Python Documentation:")
render_site("https://docs.python.org")

# 2. Embed a YouTube tutorial
print("🎥 Python Tutorial:")
render_youtube_video("https://www.youtube.com/watch?v=rfscVS0vtbw")

# 3. Embed GitHub with custom size
print("💻 GitHub:")
render_site("https://github.com", width=1200, height=700)
```

## 🏗️ Architecture

```
User (Jupyter Notebook)
        │
        ▼
    WebFrame Package
        │
 ┌──────────────┬──────────────┐
 │              │              │
site.py      video.py
render_site() render_youtube_video()
 │              │
 └──────┬───────┘
        │
  Utility Components
 ┌──────────┬───────────┬───────────┐
 │          │           │           │
validators logger   exceptions
 │          │           │
 └──────────┴───────────┘
        │
 External Dependencies
 ┌─────────────────────┐
 │ IPython.display     │
 │  • IFrame           │
 │  • HTML             │
 └─────────────────────┘
```

## 📖 API Reference

### `render_site(url, width=900, height=500, enforce_https=True)`

Render an external website inside a Jupyter Notebook cell.

**Parameters:**
- `url` (str): The URL of the website to render
- `width` (int, optional): Width of the iframe in pixels. Default: 900
- `height` (int, optional): Height of the iframe in pixels. Default: 500
- `enforce_https` (bool, optional): Whether to enforce HTTPS URLs. Default: True

**Returns:**
- `IFrame`: An IPython IFrame object

**Raises:**
- `InvalidURLError`: If the URL is invalid or doesn't meet requirements
- `ValueError`: If dimensions are invalid

### `render_youtube_video(url, width=800, height=450, autoplay=False, mute=False)`

Render a YouTube video inside a Jupyter Notebook cell.

**Parameters:**
- `url` (str): The YouTube video URL
- `width` (int, optional): Width of the video player in pixels. Default: 800
- `height` (int, optional): Height of the video player in pixels. Default: 450
- `autoplay` (bool, optional): Whether to autoplay the video. Default: False
- `mute` (bool, optional): Whether to mute the video. Default: False

**Returns:**
- `HTML`: An IPython HTML object

**Raises:**
- `InvalidYouTubeURLError`: If the YouTube URL is invalid
- `ValueError`: If dimensions are invalid

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=webframe --cov-report=html

# Run specific test file
pytest tests/test_site.py

# Run with verbose output
pytest -v
```

## 🔍 Code Quality

WebFrame uses multiple tools to ensure code quality:

```bash
# Run flake8 linting
flake8 webframe tests

# Run mypy type checking
mypy webframe

# Format code with black
black webframe tests

# Run all checks with tox
tox
```

## 📋 Requirements

- Python 3.7+
- IPython 7.0.0+


### Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/webframe.git
cd webframe

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run code quality checks
flake8 webframe tests
mypy webframe
black --check webframe tests
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

Made with ❤️
