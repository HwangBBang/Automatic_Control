# melon
import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import re


def extraction(js_code):
    # 정규식을 사용하여 숫자를 찾음
    matched = re.search(r"(\d+)", js_code)

    if matched:  # 숫자가 있다면
        return matched.group(1)  # 첫 번째로 매칭된 숫자를 출력

# 뉴진스 2집 앨범 정보 https://www.melon.com/album/detail.htm?albumId=11281456
# 뉴진스 2집 앨범 javascript:melon.link.goAlbumDetail('11281456');


# 뉴진스 아티스트 채널 https://www.melon.com/artist/timeline.htm?artistId=3114174
# 뉴진스 javascript:melon.link.goArtistDetail('3114174');


# search = input("검색어 입력: ")
# seed_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search}"

seed_url = "https://www.melon.com/chart/index.htm"

headers = {
    "User-Agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


req = requests.get(seed_url, headers=headers)
html = req.text

soup = BeautifulSoup(html, 'html.parser')

# lst50 = soup.select('.lst50')
# lst100 = soup.select('.lst100')
# lst100 = lst50 + lst100

lst100 = soup.select('.lst50, .lst100')

# lst100 = soup.find_all(class_=['lst50', 'lst100'])
# lst50 = soup.find_all(class_='lst50')
# lst100 = soup.find_all(class_='lst100')
# lst100 = lst50 + lst100

# lst100 = soup.find_all(class_=['lst50', 'lst100'])

js_code = "javascript:melon.link.goArtistDetail('3114174');"

for i in lst100:
    title = i.select_one('.ellipsis.rank01')
    artist = i.select_one('.ellipsis.rank02')
    album = i.select_one('.ellipsis.rank03')
    print(i.select_one('.rank').text, end="위 ")
    print(f" : {title.select_one('a').text} - {artist.select_one('a').text}")
    print(f"앨범 명 : {album.select_one('a').text}")
    print(
        f"아티스트 페이지 : https://www.melon.com/artist/timeline.htm?artistId={extraction(artist.select_one('a')['href'])}")
    print(
        f"앨범 페이지 : https://www.melon.com/album/detail.htm?albumId={extraction(album.select_one('a')['href'])}")
    print()
# select_one('.ellipsis.rank01').select_one('a')
# select_one('.ellipsis.rank01 a')
