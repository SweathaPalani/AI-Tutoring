#button click

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://ocs.ca/collections/dried-flower?product=8868588454196&sort_by=products_price_per_uom_asc")

time.sleep(5)  # Wait for the page to load the age verification prompt
# yes_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/form/div[2]/div/button[1]')
# yes_button.click()
# time.sleep(5) 
# Locate the login and password fields, and fill them in
month = driver.find_element(By.XPATH, "//*[@id=\"dob__month\"]")
month.send_keys("12")

day = driver.find_element(By.XPATH, "//*[@id=\"dob__day\"]")
day.send_keys("12")

year = driver.find_element(By.XPATH, "//*[@id=\"dob__year\"]")
year.send_keys("1992")
time.sleep(3) 
verify = driver.find_element(By.XPATH, "//*[@id=\"shopify-section-overlay\"]/div/section/div/div[2]/form/p[3]/button")
verify.click()

time.sleep(3) 

# product_titles = []
# product_prices = []
# for element in driver.find_elements(By.CSS_SELECTOR, "h3.product_title"):
#     product_titles.append(element.text.strip())
# # Print the extracted titles    
# print("Product Titles:")
# for title in product_titles:
#     print(title)

# for element in driver.find_elements(By.CSS_SELECTOR,"p"):
#     product_prices.append(element.text.strip())
# # Print the extracted titles    
# print("Product prices:")
# for price in product_prices:
#     print(price)

# # Close the browser window
# driver.quit()