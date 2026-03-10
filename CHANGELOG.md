# Changelog

All notable changes to the WebFrame project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-03-10

### Added

#### Core Features
- Website rendering functionality via `render_site()`
- YouTube video embedding via `render_youtube_video()`
- URL validation utilities
- HTTPS enforcement option
- Custom dimensions support for both sites and videos
- Video controls (autoplay, mute)

#### Package Infrastructure
- Complete Python package structure
- Type hints throughout the codebase
- Comprehensive docstrings
- Custom exception classes
- Configurable logging system

#### Testing
- Full test suite with pytest
- 35 test cases covering all functionality
- 91% code coverage
- Mock-based testing for IPython display

#### Code Quality
- Flake8 configuration for linting
- MyPy configuration for type checking
- Black configuration for code formatting
- Tox configuration for multi-environment testing
- Pre-configured for PEP 8 compliance

#### Documentation
- Comprehensive README with examples
- API reference documentation
- Contributing guidelines
- Quick start guide
- Usage examples file
- Architecture diagram

#### Build & Packaging
- Modern pyproject.toml configuration
- Requirements files for core and dev dependencies
- MANIFEST.in for package data
- MIT License
- .gitignore for Python projects
- py.typed marker for type checking

### Features in Detail

#### render_site()
- Validates URL format
- Enforces HTTPS by default
- Customizable iframe dimensions
- Returns IPython IFrame object
- Proper error handling and logging

#### render_youtube_video()
- Supports multiple YouTube URL formats:
  - Standard: `https://www.youtube.com/watch?v=VIDEO_ID`
  - Short: `https://youtu.be/VIDEO_ID`
  - Embed: `https://www.youtube.com/embed/VIDEO_ID`
  - Mobile: `https://m.youtube.com/watch?v=VIDEO_ID`
- Customizable player dimensions
- Autoplay and mute controls
- Returns IPython HTML object
- Proper error handling and logging

### Supported Platforms
- Python 3.7+
- Jupyter Notebook
- Google Colab
- JupyterLab

### Known Limitations
- Requires IPython environment (Jupyter/Colab)
- Some websites may block iframe embedding
- HTTPS enforcement may restrict some legacy sites

---

## [Unreleased]

### Planned Features
- Support for more video platforms (Vimeo, Dailymotion)
- PDF embedding support
- Interactive widget support
- Caching mechanisms
- Custom CSS styling options
- Responsive iframe sizing
- Error recovery mechanisms

---

[0.1.0]: https://github.com/yourusername/webframe/releases/tag/v0.1.0
