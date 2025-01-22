# Simple Web Scraper

A flexible and easy-to-use web scraping library that supports both regular HTTP requests and Selenium-based scraping. Perfect for extracting data from both static and JavaScript-rendered websites.

## Features

- Support for both regular HTTP requests and Selenium-based scraping
- Easy-to-use API for targeting specific HTML elements
- Built-in error handling and debugging capabilities
- Support for parent-child element relationships
- Customizable element property matching

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/simpleWebScraper.git
cd simpleWebScraper
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Install the package in development mode (optional):
```bash
pip install -e .
```

## Usage

Basic example:
```python
from simpleWebScraper import scrape

url = "https://example.com"
target_elem = '<span class="target">Text to extract</span>'

# For static websites
text, error = scrape(url, target_elem)

# For JavaScript-rendered websites
text, error = scrape(url, target_elem, use_selenium=True)

if error:
    print(f"Error: {error}")
else:
    print(text)
```

Advanced example with parent element:
```python
text, error = scrape(
    url,
    target_elem='<span class="target">Text</span>',
    parent_elem='<div class="parent">',
    parent_index=0,  # First matching parent
    target_index=1,  # Second matching target
    element_properties=["id", "class", "style"],
    use_selenium=True,
    debug=True
)
```

See `example.py` for a complete example that tracks YouTube subscriber counts using Social Blade.

## Requirements

- Python 3.6+
- beautifulsoup4
- selenium
- webdriver_manager
- requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.
