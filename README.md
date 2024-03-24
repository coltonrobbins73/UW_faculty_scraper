
# University Faculty Scraper

## Overview
This Python-based tool is designed to automate the process of extracting information from university faculty web pages. Specifically, it searches for indications of whether labs are accepting new permanent students, alongside extracting specific profile details. It's a helpful resource for prospective students looking to join research labs.

## Features
- **Keyword Search:** Automatically detects specific phrases indicating lab acceptance status.
- **Data Extraction:** Collects faculty profile headers, introductory paragraphs, and lab website URLs.
- **Ease of Use:** Simply input the URL of a faculty page, and the tool retrieves all relevant information.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system.
- Necessary Python libraries: `requests`, `bs4` (BeautifulSoup4), `pandas`.

You can install the required libraries using pip:

```
pip install requests beautifulsoup4 pandas
```

## Installation
Clone this repository to your local machine using:

```
git clone https://github.com/yourusername/university-faculty-scraper.git
```

Navigate into the project directory:

```
cd university-faculty-scraper
```

## Usage
To use the scraper, you'll need to execute the `scrape_and_search` function with a target URL as its argument. Here's a quick example:

```python
from scraper import scrape_and_search

url = 'http://exampleuniversity.edu/faculty/professor-profile'
datagram = scrape_and_search(url)
print(datagram)
```

Replace `'http://exampleuniversity.edu/faculty/professor-profile'` with the actual URL of the faculty page you're interested in.

## Contributing
Contributions to enhance this tool are welcome. Feel free to fork the repo and submit pull requests with your improvements. Please ensure your code adheres to the project's coding standards.

## License
This project is released under the [MIT License](LICENSE.md).

## Acknowledgments
- Thanks to BeautifulSoup and Requests libraries for making HTML parsing and web requests straightforward.
