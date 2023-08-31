from bs4 import BeautifulSoup
from urllib.request import urlopen

from urllib.parse import quote_plus  # 아스키로 변환

plusUrl = input('검색어를 입력하세요: ')
baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}'
url = baseUrl.format(quote_plus(plusUrl))


html = urlopen(url).read()  # url 을 오픈한뒤 읽어서 html 변수에 저장

soup = BeautifulSoup(html, 'html.parser')

# img_class_ = "_image _listImage"
img = soup.find_all('img')


for i in img:
    imgUrl = i['src']
    with urlopen(imgUrl) as f:
        # imgUrl 을 열어서 f 변수에 저장
        with open("./img/" + plusUrl+str(img.index(i))+'.jpg', 'wb') as h:
            # plusUrl 과 img.index(i)를 합친 파일명을 wb 형식으로 저장 하고 h 변수에 저장
            h.write(f.read())
    print(plusUrl+str(img.index(i)) + "번째 이미지 다운로드 중")

print('다운로드 완료')
