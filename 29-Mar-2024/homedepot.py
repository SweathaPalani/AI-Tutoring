from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Selenium WebDriver
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Define the URL
url = "https://www.homedepot.com/s/power%20washer"

# Navigate to the URL
driver.get(url)

try:
    # Find all price elements on the page
    price_elements = driver.find_elements(By.CLASS_NAME, 'price')

    # Print each price
    for price_element in price_elements:
        price = price_element.text.strip()
        print(price)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
