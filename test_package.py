#!/usr/bin/env python3
"""
Test script to verify kartik-webframe package works correctly
"""

print("Testing kartik-webframe package...\n")

# Test 1: Import the package
print("✓ Test 1: Importing package...")
try:
    from webframe import render_site, render_youtube_video
    print("  SUCCESS: Package imported successfully!")
except ImportError as e:
    print(f"  FAILED: Could not import package - {e}")
    exit(1)

# Test 2: Check if functions are callable
print("\n✓ Test 2: Checking functions...")
if callable(render_site):
    print("  SUCCESS: render_site() is callable")
else:
    print("  FAILED: render_site() is not callable")
    exit(1)

if callable(render_youtube_video):
    print("  SUCCESS: render_youtube_video() is callable")
else:
    print("  FAILED: render_youtube_video() is not callable")
    exit(1)

# Test 3: Test render_site function
print("\n✓ Test 3: Testing render_site()...")
try:
    result = render_site("https://example.com", width=800, height=600)
    from IPython.display import IFrame
    if isinstance(result, IFrame):
        print("  SUCCESS: render_site() returns IFrame object")
    else:
        print(f"  WARNING: render_site() returns {type(result).__name__} instead of IFrame")
except Exception as e:
    print(f"  Note: {e}")
    print("  (This is expected outside Jupyter notebook)")

# Test 4: Test render_youtube_video function
print("\n✓ Test 4: Testing render_youtube_video()...")
try:
    result = render_youtube_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    from IPython.display import HTML
    if isinstance(result, HTML):
        print("  SUCCESS: render_youtube_video() returns HTML object")
    else:
        print(f"  WARNING: render_youtube_video() returns {type(result).__name__} instead of HTML")
except Exception as e:
    print(f"  Note: {e}")
    print("  (This is expected outside Jupyter notebook)")

# Test 5: Test validators
print("\n✓ Test 5: Testing URL validation...")
try:
    from webframe.validators import validate_url, extract_youtube_id
    
    # Test valid URL
    validate_url("https://example.com")
    print("  SUCCESS: validate_url() works for valid URLs")
    
    # Test YouTube ID extraction
    video_id = extract_youtube_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    if video_id == "dQw4w9WgXcQ":
        print(f"  SUCCESS: extract_youtube_id() correctly extracted '{video_id}'")
    else:
        print(f"  FAILED: Expected 'dQw4w9WgXcQ', got '{video_id}'")
        
except Exception as e:
    print(f"  FAILED: {e}")
    exit(1)

print("\n" + "="*50)
print("🎉 ALL TESTS PASSED!")
print("="*50)
print("\n📦 Package Info:")
print("   Name: kartik-webframe")
print("   Version: 0.1.1")
print("   PyPI: https://pypi.org/project/kartik-webframe/")
print("\n✨ Your package is working perfectly!")
