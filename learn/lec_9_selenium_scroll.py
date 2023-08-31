import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

search = input("검색어 입력: ")
seed_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search}"

### [requests 로 가져오기 ]###
# req = requests.get(url)
# html = req.text
# soup = BeautifulSoup(html, 'html.parser')
############################

### [selenium으로 가져오기 ]###
driver = webdriver.Chrome()
driver.get(seed_url)  # 접속
time.sleep(3)

# 스크롤
for _ in range(10):
    driver.execute_script(
        'window.scrollTo(0,document.body.scrollHeight)')  # 스크롤
    time.sleep(1)


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# ############################


items = soup.select(".api_ani_send")

for rank, area in enumerate(items, 1):
    if area.select_one(".link_ad"):
        print("==========================================")
        print("======== 해당 게시글은 광고입니다 ========")
        print("==========================================", end="\n\n")
        continue  # 광고

    title = area.select_one(".api_txt_lines.total_tit")
    editor = area.select_one(".sub_txt.sub_name")
    print(f"=========={rank}==========")
    print(editor.text)
    print(title.text)
    print(title.get('href'), end="\n\n")
