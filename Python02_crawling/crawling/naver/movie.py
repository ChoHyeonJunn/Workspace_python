# -*- coding:utf-8 -*-

# pip install beautifulsoup4

from bs4 import BeautifulSoup
import urllib.request

#######################################

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')  # 원하는 요청으로 html 코드 가져오기
soup = BeautifulSoup(resp, 'html.parser')  # BeautifulSoup 이용하여 태그로 변환

# print(soup)

movies = soup.find_all('dl', class_='lst_dsc')
# print(movies[0])

for movie in movies:
    title = movie.find('a').text
    star = movie.find('span', class_='num').text
    print(title, '[{}]'.format(star))
