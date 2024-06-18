from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--start-maximized")
chrome_options.page_load_strategy = 'eager'

browser = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(browser, 10)

browser.get('https://the-internet.herokuapp.com/dynamic_loading/2')

button_start = browser.find_element(By.XPATH, "//button[text()='Start']")
button_start.click()

element = wait.until(EC.presence_of_element_located((By.XPATH, "//h4[text()='Hello World!']")))

search_element = browser.find_element(By.XPATH, "//h4[text()='Hello World!']")

assert element.text == 'Hello World!'
