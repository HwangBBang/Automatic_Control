from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from selenium import webdriver

search = input("검색어를 입력하세요: ")
url = f'https://www.google.com/search?q={quote_plus(search)}'


driver = webdriver.Chrome()
# webriver : 브라우저를 제어할 수 있는 라이브러리
# Chrome() : 크롬 브라우저를 제어할 수 있는 객체 생성
# driver : 크롬 브라우저를 제어할 수 있는 객체


driver.get(url)
# driver 객체를 통해 get() 메서드를 사용하여 url 을 열어줌

html = driver.page_source
# driver 객체의 page_source 는 현재 브라우저에 보이는 소스코드를 가져옴
soup = BeautifulSoup(html)


yuRUbf = soup.select(".yuRUbf")
for i in yuRUbf:
    print(i.select_one(".LC20lb.MBeuO.DKV0Md").text,
          i.a.attrs["href"], sep="\n", end="\n\n")
#  상위 클래스 yuRUbf
# 클래스 LC20lb MBeuO DKV0Md 의 text가 제목
# a태그의 속성 href 에 다음 링크
