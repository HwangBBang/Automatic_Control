# Coupang

import requests
# from urllib.request import urlopen
# from urllib.parse import quote_plus
from bs4 import BeautifulSoup

search = input("검색어를 입력: ")
seed = f'https://www.coupang.com/np/search?component=&q={search}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}

req = requests.get(seed, timeout=5, headers=headers)
# print(req.status_code)

html = req.text

soup = BeautifulSoup(html, 'html.parser')

# 광고 제품 :  search-product search-product__ad-badge
# 검색 제품 : search-product

# items = soup.select(".search-product")
items = soup.select("[class = search-product]")

rank = 1
for item in items:
    badge_rocket = item.select_one('.badge.rocket')
    if not badge_rocket:
        continue

    name = item.select_one('.descriptions .name').text
    price_value = item.select_one('.price-value')
    base_price = item.select_one('.base-price')
    link = item.select_one('.search-product-link')
    thumb = item.select_one('.search-product-wrap-img')
    # link = item.select_one('.')

    print(f'{rank}위  {name}')
    if not base_price:
        print(f'원가 : {price_value.text}원')
    else:
        print(f'원가 : {base_price.text}원 / 할인가 : {price_value.text}원')

    print(f"https://www.coupang.com/{link.get('href')}")

    if thumb.get('data-img-src'):
        imgUrl = f"https:{thumb.get('data-img-src')}"
    else:
        imgUrl = f"https:{thumb.get('src')}"

    print(imgUrl)
    print()

    imgReq = requests.get(imgUrl)
    with open(f'./img/{rank}.jpg', 'wb') as f:
        f.write(imgReq.content)

    rank += 1
