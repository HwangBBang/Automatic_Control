from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # 어떤 방식으로 찾을지
from selenium.webdriver.common.keys import Keys  # 키보드 입력을 위한 모듈
import time

# 셀레니움 옵션
options = Options()  # 옵션 객체 생성


user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
options.add_argument(f'user-agent={user_agent}')  # user_agent 변경 옵션
options.add_experimental_option('detach', True)  # 자동 꺼짐 방지 옵션
options.add_argument('--start-maximized')  # 화면 최대 크기 옵션
options.add_experimental_option(
    'excludeSwitches', ['enable-automation'])  # 상단 자동화 제어 메시

driver = webdriver.Chrome(options=options)

url = 'https://m2.melon.com/index.htm'

driver.get(url)
time.sleep(1)


# 현재 페이지가 원하는 페이지가 아니면 url을 다시 가져온다.
if driver.current_url != url:
    driver.get(url)

time.sleep(1)

driver.find_element(By.LINK_TEXT, '멜론차트').click()

for _ in range(2):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(0.5)

driver.find_elements(By.ID, 'moreBtn')[1].click()

for _ in range(2):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(0.5)


chart_list = driver.find_elements(By.CSS_SELECTOR, '#_chartList')
print(len(chart_list))
# driver.quit()  # 브라우저 닫기
