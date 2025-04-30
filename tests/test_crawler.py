import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from crawler import Crawler

def test_crawler_fetch(monkeypatch):
    class MockResponse:
        def __init__(self, text):
            self.text = text
        def raise_for_status(self): pass

    def mock_get(url):
        return MockResponse("<html><a href='/next'>Next</a></html>")

    monkeypatch.setattr("requests.get", mock_get)

    crawler = Crawler()
    result = list(crawler.crawl("http://test.com"))
    assert len(result) == 2
