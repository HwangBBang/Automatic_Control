# CGV

import requests
# from urllib.request import urlopen
# from urllib.parse import quote_plus
from bs4 import BeautifulSoup

seed = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


req = requests.get(seed, headers=headers)
html = req.text

soup = BeautifulSoup(html, 'html.parser')

# evt_osmu_lst 전체
# evt_osmu_unit 1개

movie_chart = soup.select_one('.sect-movie-chart')

movie_chart = movie_chart.select('li')


for each in movie_chart:
    # print(each.select_one('a')['href'])
    rank = each.select_one('.rank').text
    title = each.select_one('.title').text
    percent = each.select_one('.percent').get_text(" : ")
    info = each.select_one('.txt-info strong').next_element.strip()

    print(rank, f'[{title}]', sep="  ")
    print(percent)
    print(f'개봉일 : {info}')

    # print(each.select_one('.txt-info span').text.strip())
    print()
