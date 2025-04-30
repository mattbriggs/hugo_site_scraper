# Design Overview

## Architecture

- `Crawler`: Uses a Strategy pattern to define how to fetch and traverse URLs.
- `Converter`: Converts HTML to Markdown with YAML frontmatter using the Strategy pattern.
- `Writer`: Writes output files and handles directory structure.

## Extensibility

- Swap out conversion engines or parsing rules by modifying the respective Strategy classes.
- Add authentication, custom rate limiting, or content filtering by extending the crawler.

## Improvements

- Add sitemap.xml support.
- Add concurrency for faster downloads.
- Implement caching to avoid re-downloading unchanged content.
