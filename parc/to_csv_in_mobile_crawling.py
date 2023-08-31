import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus


search = input("검색어를 입력하세요: ")
url = f"https://m.search.naver.com/search.naver?where=m_blog&sm=mtb_opt&query={quote_plus(search)}&nso="


html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# soup 은 BeautifulSoup 에서 가져온 Html 전부를 의미한다.
total = soup.select(".api_txt_lines.total_tit")
# 클래스에 빈칸이 있을때 빈칸을 없애주고 . 을 찍어라


searchList = []

for i in total:

    # print(i.text)
    # print(i.attrs['href'])
    # print()
    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    searchList.append(temp)

f = open(f'{search}.csv', "w", encoding="UTF-8")
# "w": 파일을 쓰기 모드(write mode)로 열겠다는 것을 의미(파일에 새로운 내용을 씀)
csvWriter = csv.writer(f)
# csv 모듈의 writer 함수를 사용,
# 앞서 열린 파일 객체 f에 데이터를 CSV 형식으로 쓸 수 있는 csvWriter 객체를 생성

for i in searchList:
    csvWriter.writerow(i)
    # csvWriter 객체의 writerow 메서드를 사용,i에 저장된 리스트를 (CSV 형식) 한 행으로 파일에 작성
f.close()
print("complete")
