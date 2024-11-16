# 📊 Web Scraper for Nutritional Data

## Overview
This project is a Python-based web scraping tool designed to extract nutritional data from a public website using `BeautifulSoup` and `requests`. It collects detailed product information including calories, proteins, fats, and carbohydrates, and exports the data into CSV and JSON formats.

## Features
- 🌐 **Web scraping** using `BeautifulSoup` and `requests`.
- 📄 **HTML parsing** for structured data extraction.
- 💾 **CSV and JSON file generation** for data storage.
- 🛠️ **User-friendly code structure** for easy modification.

## How It Works
1. **Fetches** the webpage content using `requests`.
2. **Parses** the HTML with `BeautifulSoup` to locate nutritional tables.
3. **Extracts** product data and saves it into `.csv` and `.json` files.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/security-lab/web-scraper-health-diet.git
   ```
2. Navigate to the project directory:
   ```bash
   cd web-scraper-health-diet
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script using Python:
```bash
python main.py
```

## Requirements
- Python 3.x
- `beautifulsoup4`
- `requests`
