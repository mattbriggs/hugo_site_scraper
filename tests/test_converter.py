import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from converter import HtmlToMarkdownConverter

def test_converter_output():
    html = "<h1>Title</h1><p>Hello</p>"
    converter = HtmlToMarkdownConverter()
    markdown, metadata = converter.convert(html, "http://test.com")
    assert "Hello" in markdown
    assert metadata["url"] == "http://test.com"
