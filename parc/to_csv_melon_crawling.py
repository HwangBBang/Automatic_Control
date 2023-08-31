import csv
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from selenium import webdriver
from urllib.request import urlopen, Request

# 403 에러는 서버에서 요청을 거부했다는 의미
header = {'User-Agent': 'Mozilla/5.0'}
# 'User-Agent' 은 서버에 요청할 때 웹 브라우저를 통해 접속하는 것처럼 위장
# 'Mozilla/5.0' 은 크롬 브라우저의 버전을 의미

url = "https://www.melon.com/chart/index.htm"

req = Request(url, headers=header)
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')


###########################################################################
# lst50 = soup.select(".lst50")  # select 는 리스트로 반환
# lst100 = soup.select(".lst100")  # select 는 리스트로 반환
###########################################################################
# -> 리팩토링
lst = soup = soup.select(".lst50, .lst100")


# 클래스 lst50 : 1~50 까지의 리스트
# 클래스 lst100 : 51~100 까지의 리스트
# 클래스 wrap t_center span rank : 순위

# 클래스 ellipsis rank01 의 title : 노래이름
# 클래스 ellipsis rank02 의 title : 가수이름
# 클래스 ellipsis rank03 의 title : 앨범이름

###########################################################################
# for i in lst50:
#     print(i.select_one(".wrap.t_center span.rank").text, end="위 ")
#     print(i.select_one(".ellipsis.rank01").a.text, end=" ")
#     print(i.select_one(".ellipsis.rank02").a.text, end=" ")
#     print(i.select_one(".ellipsis.rank03").a.text)

# for i in lst100:
#     print(i.select_one(".wrap.t_center span.rank").text, end="위 ")
#     print(i.select_one(".ellipsis.rank01").a.text, end=" ")
#     print(i.select_one(".ellipsis.rank02").a.text, end=" ")
#     print(i.select_one(".ellipsis.rank03").a.text)
###########################################################################
# -> 리팩토링
for i in lst:
    print(i.select_one(".wrap.t_center span.rank").text, end="위 ")
    print(i.select_one(".ellipsis.rank01").a.text, end=" ")
    print(i.select_one(".ellipsis.rank02").a.text, end=" ")
    print(i.select_one(".ellipsis.rank03").a.text)


#################################### [CSV]###################################
melon_list = []
# f = csv(filename="melon_top100.csv", mode="w", encoding="utf-8-sig")
for i in lst:
    row = []
    row.append(i.select_one(".wrap.t_center span.rank").text)
    row.append(i.select_one(".ellipsis.rank01").a.text)
    row.append(i.select_one(".ellipsis.rank02").a.text)
    row.append(i.select_one(".ellipsis.rank03").a.text)
    melon_list.append(row)


with open("./melon_top100.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)  # f는 파일 객체, writer 에 f를 넣어서 csv 작성
    # newline="" 을 해줘야 빈 줄이 생기지 않음
    writer.writerow(["순위", "곡명", "가수", "앨범"])  # writerow 는 리스트를 한줄씩 작성
    writer.writerows(melon_list)  # writerows 는 리스트를 한번에 작성
