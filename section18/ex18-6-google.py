import time
from re import search

# import os
# import time
# import urllib.request


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys
from webdriver_manager.chrome import ChromeDriverManager


# chrome driver 자동 설치 및 서비스 생성
service = Service(ChromeDriverManager().install())

# chrome 드리아버 인스턴스 생성
driver = webdriver.Chrome(service=service)


# 드라이버를 통해 Google 페이지 접속
driver.get("https://images.google.co,kr")


# 키워드
keyword = 'cute cat'
# 검색어 입력
search_bar = driver.fine_element(By.NAME,'q')
search_bar.send_keys(keyword)
search_bar.send_keys(keys.RETRUN)

thumbnails = driver.find_element(By.CSS_SELECTOR,)

time.sleep(3)


# 드라이버 종료
driver.quit()
