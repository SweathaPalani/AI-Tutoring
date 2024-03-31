# Find all products using CSS Selector

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://webscraper.io/test-sites/e-commerce/allinone/phones")

products = driver.find_elements(By.CSS_SELECTOR, 'div.thumbnail')

for product in products:
    name = product.find_element(By.CSS_SELECTOR, 'a.title').text.strip()
    price = product.find_element(By.CSS_SELECTOR, 'h4.price').text.strip()
    print(f"Name: {name}, Price: {price}")

driver.quit()
