# SSG
import requests
# from urllib.request import urlopen
# from urllib.parse import quote_plus
from bs4 import BeautifulSoup

seed = 'https://www.ssg.com/event/eventMain.ssg'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}


req = requests.get(seed, headers=headers)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# evt_osmu_lst 전체
# evt_osmu_unit 1개

# 사이트 중지로인해 STOP
print(soup.select_one('.eo_in'))
