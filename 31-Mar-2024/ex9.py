from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Selenium WebDriver
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Define the URL of the Amazon product page you want to scrape
url = 'https://www.amazon.com/dp/B08L8KC1J7/'

# Navigate to the URL
driver.get(url)

try:
    # Extract product information like name, price, rating, etc.
    product_name = driver.find_element(By.ID, 'productTitle').text.strip()
    print('Product Name:', product_name)

except Exception as e:
    print('Error:', e)

finally:
    driver.quit()
