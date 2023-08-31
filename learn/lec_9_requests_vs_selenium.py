import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
url = 'https://section.cafe.naver.com/ca-fe/'

### [requests 로 가져오기 ]###
# req = requests.get(url)
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
############################


### [selenium으로 가져오기 ]###
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# ############################


print(html)
