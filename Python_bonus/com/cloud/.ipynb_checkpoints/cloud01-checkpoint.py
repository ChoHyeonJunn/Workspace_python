# -*- coding:utf-8 -*-

# pip install wordcloud

import json

from wordcloud import WordCloud

cloud = WordCloud(font_path='Goyang.ttf', background_color='white', max_words=30, width=400, height=300)

with open('webtoons.json', encoding='utf-8') as json_file:
    webtoon = json.load(json_file)

res = dict()
for temp in webtoon['webtoons']:
    res[temp['title']] = int(float(temp['star']) * 100) 
    # {'유미의 세포들': 980}, ...
    
visual = cloud.fit_words(res)
visual.to_image()
visual.to_file('cloud.png')
