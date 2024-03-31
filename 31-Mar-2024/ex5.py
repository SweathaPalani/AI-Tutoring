
#headless

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless") 

webdriver_service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

driver.get("https://www.nintendo.com/")

driver.quit()
