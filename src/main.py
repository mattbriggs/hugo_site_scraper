import argparse
from .crawler import Crawler
from .writer import FileWriter
from .converter import HtmlToMarkdownConverter

def main():
    parser = argparse.ArgumentParser(description='Scrape and convert a website to Hugo-compatible Markdown.')
    parser.add_argument('--url', required=True, help='The base URL to scrape.')
    parser.add_argument('--output', required=True, help='The output directory.')
    args = parser.parse_args()

    crawler = Crawler()
    converter = HtmlToMarkdownConverter()
    writer = FileWriter(args.output)

    for url, html in crawler.crawl(args.url):
        markdown, metadata = converter.convert(html, url)
        writer.write(markdown, metadata)

if __name__ == "__main__":
    main()
