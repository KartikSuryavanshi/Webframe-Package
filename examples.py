"""
WebFrame - Example Usage Script

This script demonstrates how to use WebFrame to embed websites
and YouTube videos in Jupyter notebooks.

To run this in a Jupyter notebook:
1. Install the package: pip install -e .
2. Create a new Jupyter notebook
3. Copy these code cells into your notebook
4. Run each cell to see the embedded content
"""

# Cell 1: Import the library
print("=" * 60)
print("WebFrame - Example Usage")
print("=" * 60)

from webframe import render_site, render_youtube_video

# Cell 2: Render a website with default settings
print("\n1️⃣ Rendering Python Documentation (default size):")
print("-" * 60)
render_site("https://docs.python.org")

# Cell 3: Render a website with custom dimensions
print("\n2️⃣ Rendering GitHub (custom size 1200x700):")
print("-" * 60)
render_site("https://github.com", width=1200, height=700)

# Cell 4: Render a YouTube video
print("\n3️⃣ Rendering YouTube Video:")
print("-" * 60)
render_youtube_video("https://www.youtube.com/watch?v=rfscVS0vtbw")

# Cell 5: Render a YouTube video with short URL
print("\n4️⃣ Rendering YouTube Video (short URL):")
print("-" * 60)
render_youtube_video("https://youtu.be/dQw4w9WgXcQ")

# Cell 6: Render a YouTube video with autoplay and mute
print("\n5️⃣ Rendering YouTube Video (autoplay + mute):")
print("-" * 60)
render_youtube_video(
    "https://www.youtube.com/watch?v=rfscVS0vtbw",
    width=1000,
    height=600,
    autoplay=True,
    mute=True
)

# Cell 7: Error handling example
print("\n6️⃣ Error Handling Examples:")
print("-" * 60)

try:
    # This will raise an InvalidURLError
    render_site("not a valid url")
except Exception as e:
    print(f"❌ Caught expected error: {type(e).__name__}: {e}")

try:
    # This will raise an InvalidURLError (HTTP not allowed by default)
    render_site("http://example.com")
except Exception as e:
    print(f"❌ Caught expected error: {type(e).__name__}: {e}")

try:
    # This will raise an InvalidYouTubeURLError
    render_youtube_video("https://example.com/not-youtube")
except Exception as e:
    print(f"❌ Caught expected error: {type(e).__name__}: {e}")

print("\n" + "=" * 60)
print("✅ All examples completed!")
print("=" * 60)
