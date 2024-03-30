#Headless

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Set path to chromedriver as per your configuration
webdriver_service = Service(ChromeDriverManager().install())

# Choose Chrome Webdriver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the webpage
driver.get('http://example.com')

# Wait for the page to fully load
driver.implicitly_wait(10)  # seconds

# Find elements by tag name
titles = driver.find_elements(By.TAG_NAME, 'h1')

# Print out each title text
for title in titles:
    print(title.text)

# Close the browser
driver.quit()
