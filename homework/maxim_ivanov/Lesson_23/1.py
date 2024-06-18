from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

browser.get('https://www.qa-practice.com/elements/input/simple')

input_field = browser.find_element(By.ID, 'id_text_string')
input_field.send_keys('Hello')
input_field.submit()

element = wait.until(EC.visibility_of_element_located((By.ID, 'result')))
input_field = browser.find_element(By.ID, 'result')

print(input_field.text)
