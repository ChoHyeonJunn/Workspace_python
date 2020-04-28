# -*- coding:utf-8 -*-

# pip install wordcloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import json

# cloud = WordCloud(font_path='Goyang.ttf', background_color='white', max_words=30, width=400, height=300)

with open('webtoons.json', encoding='utf-8') as file:
    webtoon = json.load(file)

res = dict()
for temp in webtoon['webtoons']:
    res[temp['title']] = int(float(temp['star']) * 100) 
    # {'유미의 세포들': 980}, ...
    
    
masking_img = np.array(Image.open('kakao.png'))
cloud = WordCloud(font_path='Goyang.ttf', max_font_size=40, mask=masking_img, background_color='white').fit_words(res)
cloud.to_file('result.png')

plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()