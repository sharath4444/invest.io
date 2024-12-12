from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Replace with your WebDriver path
driver.get("https://www.5paisa.com/nifty-100-stock-list")

# Wait for the page to load
time.sleep(5)

# Find elements containing company names
companies = driver.find_elements(By.CSS_SELECTOR, 'a#stock_name')

# Extract data
company_data = [{"company_name": company.text} for company in companies]

# Save to JSON
with open('nifty_100.json', 'w') as f:
    json.dump(company_data, f, indent=4)

# Close the driver
driver.quit()

print("Scraping completed. Data saved to 'nifty_100.json'.")
