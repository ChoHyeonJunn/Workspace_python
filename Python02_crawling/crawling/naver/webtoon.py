# -*- coding:utf-8 -*-

# pip install requests

import json
from json.decoder import JSONArray
from test.test_json.test_pass1 import JSON

from bs4 import BeautifulSoup
import requests

#######################################
resp = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=')  # 원하는 요청으로 html 코드 가져오기
soup = BeautifulSoup(resp.text, 'html.parser')  # BeautifulSoup 이용하여 태그로 변환

webtoon_list = soup.find('ul', class_='img_list')
# webtoon_list_all = webtoon_list.find_all('li')
# 
# for webtoon in webtoon_list_all:
#     title_dt = webtoon.find('dt')
#     title = title_dt.find('a').text
#     star = webtoon.find('strong').text
#     
#     temp = title_dt.find('a')
#     print('{} [{}]'.format(title, star))
#     print(temp.get('title'))

# teacher


dl = webtoon_list.select('dl')

lst = list()

for chd in dl:
    title = chd.find('a').text # 여러개라면 제일 처음 태그만 리턴
    star = chd.find('strong').text
    
    temp = {}
    temp['title'] = title
    temp['star'] = star
    lst.append(temp)
    
#     print('{} [{}]'.format(title, star))

res = {}
res['webtoons'] = lst

res_json = json.dumps(res, ensure_ascii=False)
print(res_json)

with open('webtoons.json', 'w',encoding='utf-8') as file:
    file.write(res_json)
