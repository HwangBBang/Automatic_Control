import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

search = input("검색어 입력: ")
seed_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search}"

req = requests.get(seed_url)
html = req.text

soup = BeautifulSoup(html, 'html.parser')

# total_wrap api_ani_send
# timeline_inner api_ani_send

# total_area = soup.select(".total_area")
# timeline_area = soup.select(".timeline_area")

# if total_area:
#     areas = total_area
# elif timeline_area:
#     areas = timeline_area
# else:
#     print("[NEW Area]")

items = soup.select(".api_ani_send")

for rank, area in enumerate(items, 1):
    if area.select_one(".link_ad"):
        print("==========================================")
        print("======== 해당 게시글은 광고입니다 ========")
        print("==========================================", end="\n\n")
        continue  # 광고

    title = area.select_one(".api_txt_lines.total_tit")
    editor = area.select_one(".sub_txt.sub_name")
    print(f"=========={rank}==========")
    print(editor.text)
    print(title.text)
    print(title.get('href'), end="\n\n")
