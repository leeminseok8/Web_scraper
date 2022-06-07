import requests
from bs4 import BeautifulSoup

# url 주소 요청에 대한 응답
response = requests.get("https://www.naver.com")

# 응답한 내용을 html 소스로 변경
html = response.text

# bs의 html.parser을 이용한 html 번역
soup = BeautifulSoup(html, 'html.parser')

# select(복수) | select_one(단수) 옵션이 존재
word = soup.select_one("#NM_set_home_btn")

print(word)
