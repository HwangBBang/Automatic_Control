from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()

options.add_experimental_option('detach', True)
options.add_argument('--start-maximized')
options.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = webdriver.Chrome(options=options)

url = 'https://www.naver.com/'
driver.get(url)
time.sleep(1)


# driver.find_element(By.ID)
# driver.find_element(By.CLASS_NAME)
# driver.find_element(By.CSS_SELECTOR)
# driver.find_element(By.NAME)
# driver.find_element(By.TAG_NAME)
# driver.find_element(By.XPATH)
# driver.find_element(By.LINK_TEXT)
# driver.find_element(By.PARTIAL_LINK_TEXT)


# <input id="query" name="query" type="search" title="검색어를 입력해 주세요."
# placeholder="검색어를 입력해 주세요." maxlength="255"
# autocomplete="off" class="search_input" data-atcmp-element="">

# 블랙핑크 검색후 엔터입력
# driver.find_element(
#     By.XPATH, '//*[@title="검색어를 입력해 주세요."]').send_keys("블랙핑크", Keys.ENTER)

# driver.find_element(By.XPATH, '//*[text()="VIEW"]').click()
# driver.find_element(By.LINK_TEXT, "VIEW").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "VI").click()


shortcut_items = driver.find_elements(By.CLASS_NAME, 'shortcut_item')
# print(shortcut_items)
# print()
# print(dir(shortcut_items[0]))
# print()
# print(len(shortcut_items))

time.sleep(1)
for shortcut_item in shortcut_items:
    # print(shortcut_item.get_attribute('outerHTML'))
    # print(shortcut_item.text)
    # print()
    if shortcut_item.text == '뉴스':
        shortcut_item.click()
        break

time.sleep(1)
driver.quit()
