# -*- coding:utf-8 -*-

# pip install requests

from bs4 import BeautifulSoup
import requests

#######################################

tag = input('search tag : ')
url = 'https://www.instagram.com/explore/tags/' + tag

resp = requests.get(url)  # 원하는 요청으로 html 코드 가져오기
soup = BeautifulSoup(resp.text, 'html.parser')  # BeautifulSoup 이용하여 태그로 변환
# print(soup)
img = soup.find_all('img')
print(img)