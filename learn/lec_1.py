import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

search = input("검색어 입력: ")
seed_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search}"
##################
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
# }
# req = requests.get(seed_url, headers=headers)
# print(req.request.headers)
##################

req = requests.get(seed_url)
html = req.text

soup = BeautifulSoup(html, 'html.parser')

# a = soup.select_one(".api_txt_lines.total_tit._cross_trigger")
# print(type(a)) -> bs4.element.Tag
total_area = soup.select(".total_area")
timeline_area = soup.select(".timeline_area")

# title = soup.select(".api_txt_lines.total_tit") # print(type(title)) -> bs4.element.ResultSet
# editor = soup.select(".sub_txt.sub_name")

if total_area:
    areas = total_area

elif timeline_area:
    areas = timeline_area

else:
    print("[NEW Area]")

for area in areas:
    title = area.select_one(".api_txt_lines.total_tit")
    editor = area.select_one(".sub_txt.sub_name")
    print(editor.text)
    print(title.text)
    print(title.get('href'), end="\n\n")

# print(result.get('data-cr-gdid'), end="\n") # print(result['data-cr-gdid'], end="\n")
# 선택된 태그의 속성에 접근하려면 [''] 을 이용하면된다.
# 근데 만약 해당 속성이 없으면 ? key 에러가 난다.
# 따라서 get 을 사용해 있으나 없으나 받게처리하면 된다 . (없으면 None )


#######################################################################
# dir() 함수는 파이썬에서 제공하는 내장 함수  로,
# 객체가 어떤 변수, 메서드 및 함수를 가지고 있는지 나열합니다.
# 이 함수는 주어진 객체의 모든 속성과 메서드를 나타내는 문자열의 리스트를 반환합니다.
#######################################################################

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36

# print(req.text)

# print(req.raise_for_status)
# raise_for_status 는
print(seed_url)
