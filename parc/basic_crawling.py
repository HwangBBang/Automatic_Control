
from urllib.parse import quote_plus
# urllib 이라는 라이브러리의 parse 라는 모듈 사용 (ascii 코드로 변환을 위해)
from urllib.request import urlopen
# urllib 이라는 라이브러리의 request 라는 모듈 사용
from bs4 import BeautifulSoup

seed_url = 'https://search.naver.com/search.naver?query={}&nso=&where=blog&sm=tab_opt'
plus_url = input('검색어를 입력하세요: ')
url = seed_url.format(quote_plus(plus_url))
# urllib.parse.quote_plus(plus_url) 으로 검색어를 ascii 코드로 변환
# seed_url.format() 으로 {} 안에 변환된 검색어를 넣어준다.


html = urlopen(url).read()  # url을 열어서 html 변수에 저장
# html 변수를 html.parser 를 이용해서 soup 변수에 저장
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_="api_txt_lines total_tit")
# find_all 은 해당하는 모든 태그를 찾아서 리스트 형태로 저장 / 전부 다 찾아
# find 는 해당하는 태그를 찾아서 저장 / 하나만 찾아


# BeautifulSoup 의 find_all
# BeautifulSoup 의 find
# BeautifulSoup 의 select
# BeautifulSoup 의 select_one

for i in title:
    print(i.get_text(), i['href'], sep="\n", end='\n\n')
    # get_text() 는 태그 안에 있는 텍스트만 가져오는 함수
    # print(i.text) 도 같은 기능을 한다.

    # id : sp_blog_{}
