import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Crawler:
    def __init__(self):
        self.visited = set()

    def crawl(self, base_url):
        to_visit = [base_url]

        while to_visit:
            url = to_visit.pop()
            if url in self.visited:
                continue

            try:
                response = requests.get(url)
                response.raise_for_status()
            except Exception as e:
                logger.error(f"Failed to fetch {url}: {e}")
                continue

            self.visited.add(url)
            html = response.text
            yield url, html

            soup = BeautifulSoup(html, "html.parser")
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link['href'])
                if urlparse(full_url).netloc == urlparse(base_url).netloc:
                    to_visit.append(full_url)
