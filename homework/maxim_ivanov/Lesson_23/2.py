from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

chrome_options = Options()

user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 '
              'Safari/537.36')
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--start-maximized")
chrome_options.page_load_strategy = 'eager'

browser = webdriver.Chrome(options=chrome_options)

browser.get('https://demoqa.com/automation-practice-form')


def find_element_by_id(search_browser, search_element):
    return search_browser.find_element(By.ID, search_element)


def find_element_by_xpath(search_browser, search_element):
    return search_browser.find_element(By.XPATH, search_element)


def send_keys_text(browser_element, text):
    browser_element.send_keys(text)


# Selecting first name, last name, email, number, address
field_first_name = find_element_by_id(browser, 'firstName')
field_last_name = find_element_by_id(browser, 'lastName')
field_user_email = find_element_by_id(browser, 'userEmail')
field_user_number = find_element_by_id(browser, 'userNumber')
field_address = find_element_by_id(browser, 'currentAddress')

send_keys_text(field_first_name, 'Max')
send_keys_text(field_last_name, 'Ivanov')
send_keys_text(field_user_email, 'test@yandex.ru')
send_keys_text(field_user_number, '8989767812')
send_keys_text(field_address, 'Earth')

# Selecting your date of birth
field_birth = find_element_by_id(browser, 'dateOfBirthInput')
field_birth.click()
select_year = find_element_by_xpath(browser, "//select[@class='react-datepicker__year-select']")
select_month = find_element_by_xpath(browser, "//select[@class='react-datepicker__month-select']")
select_year_chose = Select(select_year)
select_year_chose.select_by_value('1990')
select_month_chose = Select(select_month)
select_month_chose.select_by_value('4')
my_date_birthday = find_element_by_xpath(browser, "//div[@aria-label='Choose Tuesday, May 1st, 1990']")
my_date_birthday.click()

# Selecting hobbies
select_hobbies = find_element_by_xpath(browser, "//label[@for='hobbies-checkbox-1']")
select_hobbies.click()

# Selecting gender
gender = browser.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
gender.click()

# Selecting subject
field_subject = find_element_by_id(browser, 'subjectsInput')
field_subject.send_keys('Maths')
field_subject.send_keys(Keys.ENTER)

# Selecting state
field_state = find_element_by_id(browser, 'react-select-3-input')
field_state.send_keys('NCR')
field_state.send_keys(Keys.ENTER)

# Selecting city
field_city = find_element_by_id(browser, 'react-select-4-input')
field_city.send_keys('Delhi')
field_city.send_keys(Keys.ENTER)

# Submit form
button_submit = find_element_by_id(browser, 'submit')
button_submit.submit()
