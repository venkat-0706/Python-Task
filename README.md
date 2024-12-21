# Amazon Best Sellers Web Scraper

## Overview
This Python script uses Selenium to scrape product information from Amazon's Best Sellers section. It focuses on products offering discounts greater than 50% in 10 different categories and saves the data into structured formats (CSV or JSON). The script automates login using valid Amazon credentials and extracts key product details from each category.

---

## Features
- **Authentication:** Logs in to Amazon using provided credentials.
- **Data Collection:** Scrapes details of up to 1500 best-selling products from each category.
  - Product Name
  - Product Price
  - Sale Discount
  - Best Seller Rating
  - Ship From
  - Sold By
  - Rating
  - Product Description
  - Number Bought in the Past Month (if available)
  - Category Name
  - All Available Images
- **Error Handling:** Robust handling of missing elements, timeouts, and page load issues.
- **Data Storage:** Saves scraped data into a CSV or JSON file for analysis.

---

## Prerequisites
1. **Python:** Install Python 3.7 or later.
2. **Libraries:**
   - Selenium: Install using `pip install selenium`.
3. **WebDriver:**
   - Download the appropriate WebDriver (e.g., [ChromeDriver](https://chromedriver.chromium.org/downloads)) and ensure it's in your system PATH.
4. **Amazon Account:** Provide valid Amazon credentials for authentication.

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd amazon-scraper
   ```

2. **Install Dependencies:**
   ```bash
   pip install selenium
   ```

3. **Download WebDriver:**
   - Download ChromeDriver from [here](https://chromedriver.chromium.org/downloads).
   - Place it in your system PATH or the script directory.

4. **Update Credentials:**
   - Replace `your_email@example.com` and `your_password` in the script with your Amazon login credentials.

5. **Run the Script:**
   ```bash
   python amazon_scraper.py
   ```

---

## How It Works

1. **Authentication:**
   - The script navigates to the Amazon login page and authenticates using the provided email and password.

2. **Category Navigation:**
   - Visits the URLs of the 10 specified Best Seller categories.

3. **Data Extraction:**
   - Collects product details, including the name, price, rating, and more.
   - Skips products with missing or inaccessible data.

4. **Data Storage:**
   - Saves the scraped data as `amazon_best_sellers.csv` or `amazon_best_sellers.json` in the script's directory.

---

## Output Format
- **CSV File:**
  - Columns include `Name`, `Price`, `Discount`, `Rating`, `Ship From`, `Sold By`, etc.
- **JSON File:**
  - Structured JSON with the same details.

---

## Example URLs
- **Best Seller Section:**
  - [Best Sellers](https://www.amazon.in/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2)
- **Sample Categories:**
  - [Kitchen](https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_nav_kitchen_0)
  - [Shoes](https://www.amazon.in/gp/bestsellers/shoes/ref=zg_bs_nav_shoes_0)
  - [Computers](https://www.amazon.in/gp/bestsellers/computers/ref=zg_bs_nav_computers_0)
  - [Electronics](https://www.amazon.in/gp/bestsellers/electronics/ref=zg_bs_nav_electronics_0)

---

## Notes
- Scraping Amazon may violate their [Terms of Service](https://www.amazon.in/gp/help/customer/display.html). Ensure you comply with their policies.
- If the page structure changes, you may need to update the script's XPath or CSS selectors.

---

## Troubleshooting
1. **Login Issues:**
   - Ensure your credentials are correct.
   - Check for CAPTCHA prompts during login.

2. **Missing WebDriver:**
   - Verify that ChromeDriver is installed and in your PATH.

3. **Slow Page Load:**
   - Increase wait times using Selenium's `WebDriverWait`.

4. **Blocked Requests:**
   - Reduce the scraping speed to avoid being flagged by Amazon.

---

## License
This project is for educational purposes only. Use responsibly and adhere to Amazon's terms of service.

---

## Contact
For questions or suggestions, reach out to: `chanduabbireddy247@gmail.com`. 

