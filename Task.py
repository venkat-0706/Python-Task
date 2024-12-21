import time
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
service = Service('path/to/chromedriver')  # Update with your path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

AMAZON_EMAIL = 'your_email@example.com'
AMAZON_PASSWORD = 'your_password'


def login_to_amazon():
    driver.get("https://www.amazon.in/ap/signin")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ap_email"))).send_keys(AMAZON_EMAIL)
    driver.find_element(By.ID, "continue").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ap_password"))).send_keys(AMAZON_PASSWORD)
    driver.find_element(By.ID, "signInSubmit").click()


def scrape_products(category_url):
    driver.get(category_url)
    time.sleep(2)  

    products = []
    product_elements = driver.find_elements(By.CSS_SELECTOR, ".zg-item-immersion")

    for product in product_elements:
        try:
            name = product.find_element(By.CSS_SELECTOR, ".p13n-sc-truncate").text
            price = product.find_element(By.CSS_SELECTOR, ".p13n-sc-price").text
            discount = product.find_element(By.CSS_SELECTOR, ".p13n-sc-price").get_attribute("data-discount")
            rating = product.find_element(By.CSS_SELECTOR, ".a-icon-alt").text
            ship_from = product.find_element(By.CSS_SELECTOR, ".a-size-small.a-color-secondary").text
            sold_by = product.find_element(By.CSS_SELECTOR, ".a-size-small.a-color-secondary").text
            description = product.find_element(By.CSS_SELECTOR, ".a-size-small.a-color-secondary").text
            images = [img.get_attribute("src") for img in product.find_elements(By.CSS_SELECTOR, ".a-dynamic-image")]
            number_bought = product.find_element(By.CSS_SELECTOR, ".a-size-small.a-color-secondary").text

            # Check for discount greater than 50%
            if float(discount.strip('%')) > 50:
                products.append({
                    "Product Name": name,
                    "Product Price": price,
                    "Sale Discount": discount,
                    "Best Seller Rating": rating,
                    "Ship From": ship_from,
                    "Sold By": sold_by,
                    "Rating": rating,
                    "Product Description": description,
                    "Number Bought in the Past Month": number_bought,
                    "Category Name": category_url.split('/')[-1],
                    "All Available Images": images
                })
        except Exception as e:
            print(f"Error extracting product details: {e}")

    return products

def main():
    login_to_amazon()
    categories = [
        "https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_nav_kitchen_0",
        "https://www.amazon.in/gp/bestsellers/shoes/ref=zg_bs_nav_shoes_0",
        "https://www.amazon.in/gp/bestsellers/computers/ref=zg_bs_nav_computers_0",
        "https://www.amazon.in/gp/bestsellers/electronics/ref=zg_bs_nav_electronics_0",
      
    ]

    all_products = []
    for category in categories:
        products = scrape_products(category)
        all_products.extend(products)
      
    with
