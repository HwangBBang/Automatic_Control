# Daum
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus


seedUrl = 'https://news.daum.net/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

req = requests.get(seedUrl, headers=headers)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

item_issue = soup.select('.item_issue')

for each_item in item_issue:
    #
    # print(each_item.select_one('.logo_cp .thumb_g').get('alt'))  # -> 안됨
    company = each_item.select_one('.logo_cp .thumb_g').get('alt')
    department = each_item.select_one('.txt_category').text
    print(f'언론사 : {company} / {department}')
    print(each_item.select_one('.cont_thumb .tit_g .link_txt').text.strip())
    print(each_item.select_one('.cont_thumb .tit_g .link_txt').get('href'))
    print()

# item_issue cont_thumb tit_g
