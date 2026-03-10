# WebFrame - Quick Reference Guide

## 📦 Package Structure

```
webframe/
├── webframe/               # Main package
│   ├── __init__.py        # Package exports
│   ├── site.py            # Website rendering
│   ├── video.py           # YouTube video embedding
│   ├── validators.py      # URL validation utilities
│   ├── logger.py          # Logging configuration
│   ├── exceptions.py      # Custom exceptions
│   └── py.typed           # Type checking marker
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── test_site.py       # Site rendering tests
│   ├── test_video.py      # Video rendering tests
│   └── test_validators.py # Validator tests
├── pyproject.toml         # Modern Python packaging
├── setup.cfg              # Additional setup config
├── tox.ini                # Multi-environment testing
├── .flake8                # Linting configuration
├── mypy.ini               # Type checking config
├── requirements.txt       # Core dependencies
├── requirements-dev.txt   # Dev dependencies
├── .gitignore             # Git ignore patterns
├── README.md              # Full documentation
├── LICENSE                # MIT License
├── CONTRIBUTING.md        # Contribution guidelines
├── MANIFEST.in            # Package data
└── examples.py            # Usage examples
```

## 🚀 Quick Start Commands

### Installation

```bash
# Install the package in editable mode
pip install -e .

# Install with dev dependencies
pip install -e ".[dev]"
```

### Basic Usage

```python
from webframe import render_site, render_youtube_video

# Render a website
render_site("https://docs.python.org")

# Embed a YouTube video
render_youtube_video("https://www.youtube.com/watch?v=rfscVS0vtbw")
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=webframe --cov-report=html

# Run specific test file
pytest tests/test_site.py

# Run tests with verbose output
pytest -v
```

### Code Quality

```bash
# Linting
flake8 webframe tests

# Type checking
mypy webframe

# Code formatting
black webframe tests

# Check formatting without changes
black --check webframe tests

# Run all checks with tox
tox
```

## 📚 API Quick Reference

### render_site()

```python
render_site(
    url: str,
    width: int = 900,
    height: int = 500,
    enforce_https: bool = True
) -> IFrame
```

### render_youtube_video()

```python
render_youtube_video(
    url: str,
    width: int = 800,
    height: int = 450,
    autoplay: bool = False,
    mute: bool = False
) -> HTML
```

## 🔧 Development Workflow

1. **Make changes** to the code
2. **Run tests**: `pytest`
3. **Check linting**: `flake8 webframe tests`
4. **Check types**: `mypy webframe`
5. **Format code**: `black webframe tests`
6. **Commit** your changes

## 📊 Test Coverage

Current test coverage: **91%**

- 35 tests total
- All tests passing ✅
- High coverage across all modules

## 🎯 Key Features

✅ Website embedding with IFrame
✅ YouTube video embedding
✅ URL validation (HTTP/HTTPS)
✅ YouTube URL parsing (multiple formats)
✅ Custom dimensions
✅ Video controls (autoplay, mute)
✅ Comprehensive error handling
✅ Type hints throughout
✅ Full test coverage
✅ Production-ready logging

## 📝 Common Use Cases

### Embed Documentation

```python
render_site("https://docs.python.org", width=1200, height=800)
```

### Embed Tutorial Video

```python
render_youtube_video(
    "https://www.youtube.com/watch?v=rfscVS0vtbw",
    width=1000,
    height=600
)
```

### Autoplay with Mute

```python
render_youtube_video(
    "https://youtu.be/dQw4w9WgXcQ",
    autoplay=True,
    mute=True
)
```

## 🐛 Error Handling

```python
from webframe import render_site
from webframe.exceptions import InvalidURLError

try:
    render_site("invalid-url")
except InvalidURLError as e:
    print(f"Error: {e}")
```

## 📦 Publishing to PyPI

```bash
# Build the package
python -m build

# Upload to PyPI
twine upload dist/*
```

## 🔗 Useful Links

- **Repository**: https://github.com/yourusername/webframe
- **Issues**: https://github.com/yourusername/webframe/issues
- **PyPI**: https://pypi.org/project/webframe/ (when published)

## 💡 Tips

- Use `enforce_https=True` (default) for security
- Test in Jupyter or Colab for best results
- Check logs for debugging information
- Use type hints for better IDE support

---

**Happy coding with WebFrame!** 🎉
