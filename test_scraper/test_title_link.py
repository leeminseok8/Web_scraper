import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요.")
last_page = pyautogui.prompt("마지막 페이지 번호를 입력해주세요.")
page_num = 1

for i in range(1, int(last_page) * 10, 10):
    print(f"현재 {page_num}페이지 입니다.")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    # select 이용 시 list 형태로 데이터 반환
    links = soup.select(".news_tit")

    for link in links:
        title = link.text
        url = link.attrs["href"]
        print(title, url)
        
    page_num = page_num + 1
