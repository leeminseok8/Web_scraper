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

# 검색 키워드
search.send_keys("아이폰 13")
search.send_keys(Keys.ENTER)

# 스크롤 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 스크롤 최하단 이동
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    
    before_h = after_h

# 상품 정보 div
items = browser.find_elements_by_css_selector(".basicList_inner__eY_mq")

for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text
    try:
        price = item.find_element_by_css_selector(".basicList_price_area__1UXXR").text
    except:
        price = "판매중단"
    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute("href")
    print(name, price, link)