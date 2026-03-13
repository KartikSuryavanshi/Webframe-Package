#!/bin/bash

# PyPI Upload Script for WebFrame

echo "🚀 WebFrame PyPI Upload Script"
echo "================================"

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Run this from the project root."
    exit 1
fi

# Install required tools
echo "📦 Installing build tools..."
pip install --upgrade build twine

# Clean old builds
echo "🧹 Cleaning old builds..."
rm -rf dist/ build/ *.egg-info

# Build the package
echo "🔨 Building package..."
python -m build

# Check if build was successful
if [ ! -d "dist" ]; then
    echo "❌ Build failed!"
    exit 1
fi

echo "✅ Build successful!"
echo ""
echo "Choose upload destination:"
echo "1) Test PyPI (recommended for first upload)"
echo "2) Production PyPI"
echo "3) Cancel"
read -p "Enter choice (1-3): " choice

case $choice in
    1)
        echo "📤 Uploading to Test PyPI..."
        twine upload --repository testpypi dist/*
        echo ""
        echo "✅ Uploaded to Test PyPI!"
        echo "Test with: pip install --index-url https://test.pypi.org/simple/ webframe"
        ;;
    2)
        echo "📤 Uploading to Production PyPI..."
        twine upload dist/*
        echo ""
        echo "✅ Uploaded to PyPI!"
        echo "Install with: pip install webframe"
        ;;
    3)
        echo "❌ Upload cancelled"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac
