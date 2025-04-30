# Hugo Site Scraper

This Python script crawls a website starting from a user-provided URL, downloads the content, converts it to Markdown with YAML frontmatter compatible with Hugo, and saves it to a specified folder.

## Features

- CLI with `argparse`
- Object-Oriented Design
- Software Design Patterns (Factory, Strategy)
- Logging and error handling
- Unit testing with `pytest`

## Usage

```bash
python -m src.main --url "https://example.com" --output "./output"
```

## Running Tests

```bash
pytest tests/
```
