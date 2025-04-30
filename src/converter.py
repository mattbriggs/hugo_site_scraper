import html2text
import yaml

class HtmlToMarkdownConverter:
    def convert(self, html, url):
        converter = html2text.HTML2Text()
        converter.ignore_links = False
        markdown_body = converter.handle(html)

        metadata = {
            "title": url.split("/")[-1] or "index",
            "url": url
        }
        yaml_header = yaml.dump(metadata, sort_keys=False)

        markdown = f"---\n{yaml_header}---\n{markdown_body}"
        return markdown, metadata
