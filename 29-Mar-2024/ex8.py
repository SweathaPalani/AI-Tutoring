# selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setting up Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get('http://example.com')

# Wait for the page to fully load (if needed you can use explicit waits with WebDriverWait)
driver.implicitly_wait(10) # seconds

# Find elements and perform actions
titles = driver.find_elements(By.TAG_NAME, 'h1')

# Print out each title text
for title in titles:
    print(title.text)

# Close the browser
driver.quit()
