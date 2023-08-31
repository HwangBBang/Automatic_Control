from urllib.request import urlopen  # url 을 열기 위해
from bs4 import BeautifulSoup  # html 을 파싱하기 위해
from urllib.parse import quote_plus  # 아스키로 변환을 위해
from selenium import webdriver  # 웹 드라이버를 사용하기 위해
from selenium.webdriver.chrome.options import Options  # 웹 드라이버 옵션을 사용하기 위해
import time  # 시간을 사용하기 위해


seedUrl = "https://www.instagram.com/explore/tags/{}/?hl=ko"
plusUrl = input("검색어 입력: ")

url = seedUrl.format(quote_plus(plusUrl))

# 셀레니움의 웹 드라이버를 사용하는 이유
# 이제는 리액트js 를 사용하는 웹사이트가 많아서 웹 페이지가 정적 -> 동적으로 바뀌었다,
# requests 를 사용하면 정적인 웹 페이지를 가져와 beautifulsoup 으로 파싱을 하였는데
# js 로 이뤄진 웹페이지는 다른 방법이 필요하다.
# 셀레니움은 웹 드라이버를 사용하여 웹 페이지를 가져온다.


# ==============옵션 설정================
options = Options()
options.add_argument("--start-maximized")  # 전체화면으로 실행
options.add_experimental_option("detach", True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option(
    "excludeSwitches", ["enable-logging"])  # 불필요한 메시지 제거
# =====================================

driver = webdriver.Chrome(options=options)
driver.get(url)

time.sleep(3)

html = driver.page_source
# driver의 페이지 소스를 가져와서 html 변수에 저장
soup = BeautifulSoup(html, features="html.parser")
insta = soup.select('._aabd._aa8k._al3l')

driver.close()  # 드라이버 닫기


for i in insta:
    print("https://www.instagram.com/" + i.a['href'])  # i의 a태그에 href 속성을 가져온다.
    # i의 _aagv 클래스를 찾아서 img 태그의 src 속성을 가져온다.
    imgUrl = i.select_one('._aagv').img['src']
    with urlopen(imgUrl) as f:
        # imgUrl 을 열어서 f 변수에 저장
        with open("./img/" + plusUrl + str(insta.index(i)) + ".jpg", "wb") as h:
            # plusUrl 과 insta.index(i)를 합친 파일명을 wb 형식으로 저장 하고 h 변수에 저장
            # wb 는 write binary 의 약자로 바이너리 형식으로 저장한다는 뜻(이미지, 동영상 등)
            h.write(f.read())
    print()
    print(plusUrl, str(insta.index(i)) + " 번째 이미지 다운로드 중", end="\n\n")
