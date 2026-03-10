# Contributing to WebFrame

Thank you for your interest in contributing to WebFrame! This document provides guidelines and instructions for contributing.

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip
- git

### Setting Up Development Environment

1. **Fork and clone the repository**

```bash
git clone https://github.com/yourusername/webframe.git
cd webframe
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install development dependencies**

```bash
pip install -e ".[dev]"
```

4. **Verify installation**

```bash
pytest
```

## 📋 Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Your Changes

- Write clean, readable code
- Follow PEP 8 style guidelines
- Add type hints to all functions
- Write docstrings for all public functions and classes
- Add tests for new functionality

### 3. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=webframe --cov-report=html

# Run specific test file
pytest tests/test_site.py
```

### 4. Run Code Quality Checks

```bash
# Linting with flake8
flake8 webframe tests

# Type checking with mypy
mypy webframe

# Format code with black
black webframe tests

# Run all checks with tox
tox
```

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add amazing new feature"
```

**Commit Message Format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Test changes
- `refactor:` - Code refactoring
- `style:` - Code style changes
- `chore:` - Maintenance tasks

### 6. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## 🧪 Testing Guidelines

- Write tests for all new features
- Ensure all tests pass before submitting PR
- Aim for high test coverage (>80%)
- Use descriptive test names
- Mock external dependencies (like IPython display)

**Test Structure:**

```python
class TestYourFeature:
    """Test cases for your feature."""

    def test_basic_functionality(self):
        """Test basic functionality."""
        # Arrange
        ...
        # Act
        ...
        # Assert
        ...
```

## 📝 Code Style

### Python Code Style

- Follow PEP 8
- Use type hints
- Maximum line length: 88 characters (Black default)
- Use meaningful variable names
- Write docstrings for public APIs

**Example:**

```python
def render_site(
    url: str,
    width: int = 900,
    height: int = 500,
    enforce_https: bool = True
) -> IFrame:
    """
    Render an external website inside a Jupyter Notebook cell.

    Args:
        url: The URL of the website to render
        width: Width of the iframe in pixels (default: 900)
        height: Height of the iframe in pixels (default: 500)
        enforce_https: Whether to enforce HTTPS URLs (default: True)

    Returns:
        IFrame: An IPython IFrame object

    Raises:
        InvalidURLError: If the URL is invalid
    """
    ...
```

### Documentation Style

- Use Google-style docstrings
- Include type information
- Provide examples where helpful
- Document all parameters and return values
- List all exceptions that can be raised

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Description** - Clear description of the bug
2. **Steps to Reproduce** - Minimal steps to reproduce the issue
3. **Expected Behavior** - What you expected to happen
4. **Actual Behavior** - What actually happened
5. **Environment** - Python version, OS, package version
6. **Code Sample** - Minimal code that reproduces the issue

## 💡 Suggesting Features

When suggesting features, please include:

1. **Use Case** - Why is this feature needed?
2. **Proposed Solution** - How should it work?
3. **Alternatives** - Any alternative solutions considered?
4. **Additional Context** - Any other relevant information

## 📦 Project Structure

```
webframe/
├── webframe/           # Main package
│   ├── __init__.py    # Package initialization
│   ├── site.py        # Website rendering
│   ├── video.py       # Video embedding
│   ├── validators.py  # URL validation
│   ├── logger.py      # Logging utilities
│   └── exceptions.py  # Custom exceptions
├── tests/             # Test suite
│   ├── test_site.py
│   ├── test_video.py
│   └── test_validators.py
├── pyproject.toml     # Package configuration
├── README.md          # Documentation
└── LICENSE            # License file
```

## ✅ Pull Request Checklist

Before submitting your PR, ensure:

- [ ] Code follows PEP 8 style guidelines
- [ ] All tests pass (`pytest`)
- [ ] Code is properly formatted (`black webframe tests`)
- [ ] No linting errors (`flake8 webframe tests`)
- [ ] Type checking passes (`mypy webframe`)
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Commit messages are descriptive
- [ ] PR description explains the changes

## 🤝 Code Review Process

1. Maintainers will review your PR
2. They may suggest changes or ask questions
3. Make requested changes and push new commits
4. Once approved, your PR will be merged

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Your contributions make WebFrame better for everyone. Thank you for taking the time to contribute!

## 📞 Questions?

If you have questions, feel free to:
- Open an issue
- Start a discussion
- Reach out to maintainers

---

Happy coding! 🎉
