
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service 필요 없어짐
# from webdriver_manager.chrome import ChromeDriverManager 필요 없어짐

options = Options()
options.add_argument("--start-maximized")  # 전체화면으로 실행
options.add_argument("--headless=new")  # 브라우저 안 뜨게
options.add_experimental_option("detach", True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option(
    "excludeSwitches", ["enable-logging"])  # 불필요한 메시지 제거

# service = Service(ChromeDriverManager(path="DRIVER").install())

# print(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)
driver.get("https://naver.com")


print(driver.title)
