"""Grid layout embedding for Jupyter notebooks."""

from IPython.display import display, HTML
from webframe.validators import validate_url


def render_grid(urls, width=400, height=300, ncols=2): 
    """Display multiple URLs in a grid layout using iframes.

    Args:
        urls: List of URLs to embed
        width: Width of each iframe (default 400)
        height: Height of each iframe (default 300)
        ncols: Number of columns in the grid (default 2)
    """
    if not isinstance(urls, list):
        display(HTML('<div style="color:red;">urls must be a list of URLs</div>'))
        return
    ncols = max(1, int(ncols))
    html = '<table style="border-spacing:10px;"><tr>'
    col = 0
    for url in urls:
        if not validate_url(url): 
            html += f'<td><div style="color:red;">Invalid URL:<br>{url}</div></td>' 
        else: 
            html += ( 
                f'<td><iframe src="{url}" width="{width}" height="{height}" ' 
                'style="border:1px solid #ccc;"></iframe></td>' 
            ) 
        col += 1 
        if col == ncols: 
            html += '</tr><tr>' 
            col = 0 
    html += '</tr></table>'
    display(HTML(html))
