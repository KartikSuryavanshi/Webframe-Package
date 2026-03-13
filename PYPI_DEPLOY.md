# PyPI Deployment Guide

## Prerequisites

1. **Create PyPI Account**
   - Go to https://pypi.org/account/register/
   - Verify your email

2. **Create Test PyPI Account (Optional but Recommended)**
   - Go to https://test.pypi.org/account/register/
   - This lets you test uploads before going live

## Setup PyPI API Token

1. Log in to PyPI
2. Go to Account Settings → API Tokens
3. Create a new API token:
   - Token name: `webframe-package`
   - Scope: `Entire account` (or specific to this project after first upload)
4. **Copy the token immediately** (you won't see it again)

## Add Token to GitHub

1. Go to your GitHub repository
2. Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `PYPI_API_TOKEN`
5. Value: Paste your PyPI token
6. Click "Add secret"

## Manual Upload (First Time)

Before using GitHub Actions, do a manual upload first:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Upload to Test PyPI (optional)
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

You'll be prompted for username (use `__token__`) and password (paste your API token).

## Automated Upload via GitHub Actions

After manual setup, GitHub Actions will auto-publish on new releases:

1. Go to your GitHub repository
2. Click "Releases" → "Create a new release"
3. Tag version: `v0.1.0`
4. Release title: `v0.1.0`
5. Description: Brief changelog
6. Click "Publish release"

GitHub Actions will automatically build and upload to PyPI!

## Versioning

Update version in `pyproject.toml` before each release:

```toml
version = "0.1.1"  # Increment this
```

## Verify Installation

After publishing:

```bash
pip install webframe
```

Test it works:

```python
from webframe import render_site
```

## Troubleshooting

**Error: "File already exists"**
- You can't re-upload the same version
- Increment version number in pyproject.toml

**Error: "Invalid credentials"**
- Double-check your API token in GitHub secrets
- Make sure username is `__token__` (literal string)

**Package not found after upload**
- Wait 1-2 minutes for PyPI to index it
- Check https://pypi.org/project/webframe/
