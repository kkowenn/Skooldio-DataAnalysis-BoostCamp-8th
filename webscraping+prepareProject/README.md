# Web Scraping and Data Preparation for Analysis Project

## Introduction
Web scraping in Thailand is legally ambiguous, so exercise caution and responsibility while conducting this project. Each team member is assigned a specific website to scrape individually. Follow the detailed steps below to ensure consistency and accuracy in data collection.

## Steps for Web Scraping

1. **Install Scrapy.io**
   - Ensure Scrapy.io is installed on your system to begin the scraping process.

2. **Inspect the Website**
   - Open Google Chrome.
   - Navigate to the target website.
   - Right-click anywhere on the webpage and select "Inspect".

3. **Web Scraper Configuration**
   - In the Inspect panel, find and click on the "Web Scraper" tab.
   - Click "Create new sitemap" and then "Import sitemap".
   - Configure your sitemap according to the website structure.

4. **Scrape the Website**
   - Once the sitemap is configured, click "Scrape".
   - Wait for the scraping process to complete.
   - Export the scraped data for further processing.

### Data Storage
All scraped data links are stored:
#### All Scrape Links

## Data Cleaning

After scraping, clean the data to ensure it is ready for analysis. The cleaning process involves:
- Removing null, NaN, or empty data from relevant columns.
- Merging datasets together.
- Dropping duplicate titles.

### Cleaned Data Result
The cleaned data is stored and visualized here:

## Data Preparation and Analysis

To enhance the dataset for analysis, additional processing steps are performed, including the use of NLP (Natural Language Processing) techniques. Specifically, NLPthai is utilized to count the number of Thai and English words in the new data. This helps in understanding the linguistic distribution within the dataset.

### Relational Database Model Design
To facilitate easier analysis, prepare and design relational database tables. This structured approach helps in organizing and retrieving data efficiently.




