'''
BeautifulSoup
    Html, xml 등의 마크업 언어를 파싱하는 라이브러리
    ex) <html>내용</html>

    BeautifulSoup 설치 방법
    pip install beautifulsoup4
'''
from http.client import responses

import requests
from bs4 import BeautifulSoup
# https://m.news.nate.com/hissue/groupList?mid=m01&isq=11221&sisq=11217#cid1089625
url = 'https://m.news.nate.com/hissue/groupList'
params = {
    'mid':'m01',
    'isq':'11221',
    'sisq': '11217'
}

response = requests.get(url, params = params)
html = response.text

soup = BeautifulSoup(html,'html.parser')
tit_list = soup.find_all('h2')
for idx, tit in enumerate(tit_list):
    print(f'{idx+1}:{tit.text.strip()}')

