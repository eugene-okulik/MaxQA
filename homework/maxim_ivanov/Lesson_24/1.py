from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()

user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 '
              'Safari/537.36')
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--start-maximized")
chrome_options.page_load_strategy = 'normal'

browser = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(browser, 10)

browser.get('https://www.demoblaze.com/index.html')

href_value = "prod.html?idp_=1"
xpath = f"//a[@href='{href_value}']"
element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

ActionChains(browser).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()

browser.switch_to.window(browser.window_handles[1])

add_to_cart = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-success btn-lg']"))
)

add_to_cart.click()

alert = wait.until(EC.alert_is_present())
alert.accept()
browser.close()

browser.switch_to.window(browser.window_handles[0])
cart = browser.find_element(By.XPATH, "//a[contains(text(),'Cart')]")
cart.click()

find_element = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//td[text()='Samsung galaxy s6']"))
)

assert find_element.text == 'Samsung galaxy s6'
