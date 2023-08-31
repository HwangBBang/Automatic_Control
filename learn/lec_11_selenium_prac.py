from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # 어떤 방식으로 찾을지
from selenium.webdriver.common.keys import Keys  # 키보드 입력을 위한 모듈
import time

# 셀레니움 옵션
options = Options()  # 옵션 객체 생성


#########################       화면 관련        ###############################
options.add_experimental_option('detach', True)  # 자동 꺼짐 방지 옵션
options.add_argument('--start-maximized')  # 화면 최대 크기 옵션
options.add_experimental_option(
    'excludeSwitches', ['enable-automation'])  # 상단 자동화 제어 메시지 제거 옵션


driver = webdriver.Chrome(options=options)  # 적용

url = f"https://naver.com"

driver.get(url)

# 검색창에 자동으로 검색어 입력
# driver.find_element(By.ID, 'query').send_keys('파이썬')
driver.find_element(By.CSS_SELECTOR, '#query').send_keys('뉴진스')
time.sleep(1)

# 입력한 검색어 검색하기(검색 버튼 클릭)
# driver.find_element(By.CLASS_NAME, 'btn_search').click()
driver.find_element(By.CSS_SELECTOR, '.btn_search').click()
time.sleep(1)

# 'VIEW' 텍스트를 가진 요소 클릭하기
driver.find_element(By.XPATH, "//*[text()='VIEW']").click()
time.sleep(1)

# 검색창에 입력된 검색어 지우기
driver.find_element(By.NAME, 'query').clear()
time.sleep(1)

# 검색창에 다시 검색어 입력하기
driver.find_element(By.NAME, 'query').send_keys('아이브')
time.sleep(1)

# 입력된 검색어에서 엔터키 입력하기
driver.find_element(By.NAME, 'query').send_keys(Keys.ENTER)
time.sleep(1)

# 바디에서 엔드키 입력하기
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
time.sleep(1)

# 바디에서 홈키 입력하기
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
time.sleep(1)

# 바디에서 페이지다운키 입력하기
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# 바디에서 페이지다운키 입력하기
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
time.sleep(1)

# 스크린샷 찍기
driver.save_screenshot('/Users/hwangbyeonghun/Desktop/Crawling/img/naver.png')
driver.quit()
