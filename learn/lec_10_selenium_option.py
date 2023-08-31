from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 셀레니움 옵션
options = Options()  # 옵션 객체 생성


#########################       화면 관련        ###############################
options.add_experimental_option('detach', True)  # 자동 꺼짐 방지 옵션

options.add_argument('--start-maximized')  # 화면 최대 크기 옵션
# options.add_argument('--start-fullscreen')  # 화면 전체 화면 옵션
# options.add_argument('window-size=300,300')  # 화면 300x300 옵션

# options.add_argument('--headless')  # 화면 자체를 안띄우기 옵션


#############################################################################
# options.add_argument('--mute-audio')  # 음소거 옵션
# options.add_argument('incognito')  # 시크릿모드 옵션
options.add_experimental_option(
    'excludeSwitches', ['enable-automation'])  # 상단 자동화 제어 메시지 제거 옵션
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 상단 자동화 제어 메시지 제거 옵션
#############################################################################

######################       user_agent옵션        ###########################
# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.0.0 Safari/537.36'
# options.add_argument(f'user-agent={user_agent}')  # user_agent 변경 옵션
#############################################################################

######################       user_data 옵션        ###########################
user_data_dir = '/Users/hwangbyeonghun/Desktop/Crawling/hwangbbang'
options.add_argument(f'user-data-dir={user_data_dir}')  # user_data_dir 옵션
# user_data 를 사용해 log 를 유지할 수 있다.
#############################################################################


driver = webdriver.Chrome(options=options)  # 적용

url = f"https://naver.com"

driver.get(url)


# driver.quit()  # 브라우저 닫기
