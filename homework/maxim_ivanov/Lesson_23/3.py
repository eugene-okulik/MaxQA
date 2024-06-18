from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_options = Options()

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument("--start-maximized")
chrome_options.page_load_strategy = 'eager'

browser = webdriver.Chrome(options=chrome_options)

browser.get('https://www.qa-practice.com/elements/select/single_select')


def find_element_by_id(search_browser, search_element):
    return search_browser.find_element(By.ID, search_element)


select_language = find_element_by_id(browser, 'id_choose_language')
select_language_chose = Select(select_language)

language = 'Python'

select_language_chose.select_by_visible_text(language)

# Submit form
button_submit = find_element_by_id(browser, 'submit-id-submit')
button_submit.submit()

field_result = find_element_by_id(browser, 'result-text')

assert field_result.text == language
