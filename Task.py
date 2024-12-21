import time
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def configure_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=options)
    return driver
    
def authenticate(driver, email, password):
    driver.get("https://www.amazon.in/ap/signin")
    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_email"))
        )
        email_field.send_keys(email)
        driver.find_element(By.ID, "continue").click()

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ap_password"))
        )
        password_field.send_keys(password)
        driver.find_element(By.ID, "signInSubmit").click()
    except TimeoutException:
        print("Login elements not found. Check your credentials or internet connection.")
        driver.quit()
        exit()


def scrape_category(driver, category_url):
    driver.get(category_url)
    time.sleep(5)  
    
    scraped_data = []
    
    try:
        products = driver.find_elements(By.XPATH, "//div[contains(@class, 'zg-grid-general-faceout')]")
        for product in products[:1500]:  
            try:
                name = product.find_element(By.CSS_SELECTOR, ".p13n-sc-truncate-desktop-type2").text
                price = product.find_element(By.CSS_SELECTOR, ".p13n-sc-price").text
                discount = None  
                rating = product.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text
                ship_from = None  
                sold_by = None  
                description = None  
                num_bought = None 
                images = None  

                # Append collected data
                scraped_data.append({
                    "Name": name,
                    "Price": price,
                    "Discount": discount,
                    "Rating": rating,
                    "Ship From": ship_from,
                    "Sold By": sold_by,
                    "Description": description,
                    "Number Bought": num_bought,
                    "Images": images,
                })
            except NoSuchElementException:
                continue  
    except TimeoutException:
        print("Failed to load products in the category. Check your connection or the URL.")
    
    return scraped_data


def save_data(data, file_format="csv", filename="amazon_best_sellers"):
    if file_format == "csv":
        keys = data[0].keys()
        with open(f"{filename}.csv", "w", newline="", encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    elif file_format == "json":
        with open(f"{filename}.json", "w", encoding="utf-8") as output_file:
            json.dump(data, output_file, indent=4)

if __name__ == "__main__":
    # Amazon credentials
    email = "your_email@example.com"
    password = "your_password"

    
    categories = [
        "https://www.amazon.in/gp/bestsellers/kitchen/ref=zg_bs_nav_kitchen_0",
        "https://www.amazon.in/gp/bestsellers/shoes/ref=zg_bs_nav_shoes_0",
        "https://www.amazon.in/gp/bestsellers/computers/ref=zg_bs_nav_computers_0",
        "https://www.amazon.in/gp/bestsellers/electronics/ref=zg_bs_nav_electronics_0",
        
    ]

    driver = configure_driver()
    try:
        authenticate(driver, email, password)
        all_scraped_data = []
        
        for category_url in categories[:10]:  # Limit to 10 categories
            print(f"Scraping category: {category_url}")
            category_data = scrape_category(driver, category_url)
            all_scraped_data.extend(category_data)

        save_data(all_scraped_data, file_format="csv", filename="amazon_best_sellers")
        print("Scraping completed successfully. Data saved to file.")
    finally:
        driver.quit()
