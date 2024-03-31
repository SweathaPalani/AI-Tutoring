#button click

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://emblemcannabis.com/collection/cannabis-oil/")

time.sleep(5)  # Wait for the page to load the age verification prompt
yes_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/form/div[2]/div/button[1]')
yes_button.click()
time.sleep(5) 
# time.sleep(2)
# yes_button = driver.find_element(By.XPATH, "//*[@id=\"content\"]/div[1]/div/div/div[3]/button")
# yes_button.click()

product_titles = []
product_prices = []
for element in driver.find_elements(By.CSS_SELECTOR, "h3.product_title"):
    product_titles.append(element.text.strip())
# Print the extracted titles    
print("Product Titles:")
for title in product_titles:
    print(title)

for element in driver.find_elements(By.CSS_SELECTOR,"p"):
    product_prices.append(element.text.strip())
# Print the extracted titles    
print("Product prices:")
for price in product_prices:
    print(price)

# Close the browser window
driver.quit()