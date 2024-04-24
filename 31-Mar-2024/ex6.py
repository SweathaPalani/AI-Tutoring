from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

webdriver_service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=webdriver_service)

driver.get("https://news.ycombinator.com/login")

# Locate the login and password fields, and fill them in
month = driver.find_element(By.XPATH, "//*[@id=\"dob__month\"]")
month.send_keys("12")

day = driver.find_element(By.XPATH, "//*[@id=\"dob__day\"]")
day.send_keys("12")

year = driver.find_element(By.XPATH, "//*[@id=\"dob__year\"]")
year.send_keys("1992")

verify = driver.find_element(By.XPATH, "//*[@id=\"shopify-section-overlay\"]/div/section/div/div[2]/form/p[3]/button")
verify.click()



driver.quit()
