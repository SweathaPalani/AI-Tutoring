# Find all products using XPath

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://webscraper.io/test-sites/e-commerce/allinone/phones")


products = driver.find_elements(By.XPATH, '//div[contains(@class,"thumbnail")]')


for product in products:
    name = product.find_element(By.XPATH, './/a[contains(@class,"title")]').text.strip()
    price = product.find_element(By.XPATH, './/h4[contains(@class,"float-end price card-title pull-right")]').text.strip()
    print(f"Name: {name}, Price: {price}")


driver.quit()
