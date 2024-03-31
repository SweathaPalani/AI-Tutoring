from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

webdriver_service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=webdriver_service)

driver.get("https://news.ycombinator.com/login")

# Locate the login and password fields, and fill them in
login_field = driver.find_element(By.XPATH, "//input[@type='text']")
login_field.send_keys("sweathaa")

password_field = driver.find_element(By.XPATH, "//input[@type='password']")
password_field.send_keys("sweathaa")

submit_button = driver.find_element(By.XPATH, "//input[@value='login']")
submit_button.click()

driver.save_screenshot('screenshot.png')

driver.quit()
