from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 생성
browser = webdriver.Chrome("/Users/minxi/Desktop/Repository/chromedriver/chromedriver")

# 웹사이트 열기
browser.get("https://www.naver.com")

# 로딩이 끝날 때 까지 최대 n초 대기
browser.implicitly_wait(3)

# 쇼핑 메뉴 클릭
browser.find_element_by_css_selector("a.nav.shop").click()
time.sleep(1)

# 검색창 클릭
search = browser.find_element_by_css_selector("input._searchInput_search_input_QXUFf")
search.click()

search.send_keys("아이폰 13")
search.send_keys(Keys.ENTER)