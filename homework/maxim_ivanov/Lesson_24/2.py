from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()

user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 '
              'Safari/537.36')
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--start-maximized")
chrome_options.page_load_strategy = 'eager'

browser = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(browser, 10)

browser.get('https://magento.softwaretestingboard.com/gear/bags.html')

elements = browser.find_elements(By.XPATH, "//div[@data-price-box='product-id-14']")
element = elements[0]

actions = ActionChains(browser)

actions.move_to_element(element).perform()

products = browser.find_elements(By.XPATH, "//a[@title='Add to Compare' and @title='Add to Compare']")

if products:
    first_product = products[0]

    add_to_compare_button = first_product.find_element(By.XPATH, "//a[@aria-label='Add to Compare']")

    add_to_compare_button.click()

    compare_products_list = browser.find_elements(By.XPATH, "//a[@class='product-item-link']")
    compare_product = compare_products_list[0]

    assert compare_product.text == 'Push It Messenger Bag'
