# -*- coding:utf-8 -*-

# pip install requests

from bs4 import BeautifulSoup
import requests

#######################################
resp = requests.get('https://www.iei.or.kr/intro/teacher.kh')  # 원하는 요청으로 html 코드 가져오기
soup = BeautifulSoup(resp.text, 'html.parser')  # BeautifulSoup 이용하여 태그로 변환

teacher = soup.find('div', class_='intro_list')
list = teacher.find_all('li')

for li in list:
    img = li.find('img').get('src')
    intro_name = li.find('p',class_='intro_name').text
    print('[{}] [{}]'.format(intro_name, img))

# teacher


# dl = webtoon_list.select('dl')
# 
# lst = list()
# 
# for chd in dl:
#     title = chd.find('a').text # 여러개라면 제일 처음 태그만 리턴
#     star = chd.find('strong').text
#     
#     temp = {}
#     temp['title'] = title
#     temp['star'] = star
#     lst.append(temp)
#     
# #     print('{} [{}]'.format(title, star))
# 
# res = {}
# res['webtoons'] = lst
# 
# res_json = json.dumps(res, ensure_ascii=False)
# print(res_json)
# 
# with open('webtoons.json', 'w',encoding='utf-8') as file:
#     file.write(res_json)
