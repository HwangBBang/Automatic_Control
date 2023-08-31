import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# search = input("검색어 입력: ")
# seed_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search}"
seed_url = "https://www.naver.com/"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


req = requests.get(seed_url, headers=headers)
html = req.text

soup = BeautifulSoup(html, 'html.parser')

# [태그 선택하기]

# print(soup.h1)
# print(soup.find('h1'))
# print(soup.select_one('h1'))
# print(soup.select_one('.search_logo'))
# print(soup.select_one('#special-input-logo'))
# print(soup.find(class_='search_logo'))
# print(soup.find(id='special-input-logo'))
