from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector
import time

# MySQL Configuration
db_config = {
    "host": "localhost",     # Change if not running on local
    "user": "root",          # Replace with your username
    "password": "1234",  # Replace with your password
    "database": "StockMarket"
}

# Connect to the database
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    print("Connected to MySQL database!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure your WebDriver path is set
driver.get("https://www.5paisa.com/nifty-100-stock-list")

# Wait for the page to load
time.sleep(5)

# Scrape data
companies = driver.find_elements(By.CSS_SELECTOR, 'a#stock_name')
company_data = [{"company_name": company.text} for company in companies]

# Insert data into the database
try:
    for company in company_data:
        sql_query = "INSERT INTO Nifty100Stocks (company_name) VALUES (%s)"
        cursor.execute(sql_query, (company["company_name"],))
    connection.commit()
    print("Data inserted successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the database connection
    cursor.close()
    connection.close()
    driver.quit()
