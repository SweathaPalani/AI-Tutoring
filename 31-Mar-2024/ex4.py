#pagination

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

base_url = "http://quotes.toscrape.com/page/"

# Number of pages to scrape
num_pages = 3

for i in range(1, num_pages + 1):
    url = f"{base_url}{i}"
    driver.get(url)
    time.sleep(2)

    # Scrape quotes and authors
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        print(f"{text} — {author}")


driver.quit()

