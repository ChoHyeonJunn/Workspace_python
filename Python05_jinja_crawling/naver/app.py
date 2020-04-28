# -*- coding:utf-8 -*-

# pip install Jinja2 
# Jinja2 는 flask install 하며 자동으로 같이 install 된다!

# application : Contoller 역할을 하는 부분이다!
# templates : html 파일들이 들어간다.
# static : css , js 등이 들어간다.

'''
CORS Cross Origin

요청 측에서 cors 해결 시도시 어렵다
응답하는 측에서 cors 해결 시도시 간단!!

wireShark 해보기!!
'''

from bs4 import BeautifulSoup
from flask import Flask, request, render_template
import urllib.request
import json
# pip install flask_cors
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r'*':{'origins':'*'}})


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/crawling')
def crawling():
    # naver movie list를 Crawling 해오자
    resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn#')  # 원하는 요청으로 html 코드 가져오기
    soup = BeautifulSoup(resp, 'html.parser')  # BeautifulSoup 이용하여 태그로 변환
    
    movies = soup.find_all('dl', class_='lst_dsc')
    
    lst = list()
    for movie in movies:
        title = movie.find('a').text
        star = movie.find('span', class_='num').text
        
        temp = {}
        temp['title'] = title
        temp['star'] = star
        lst.append(temp)

    # crawling 된 데이터를 dictionary에 {movies: [{title: 제목, star: 별점}, ...]} 로 저장하자
    res = {}
    res['movies'] = lst    
    
    # json으로 변환하여 리턴하자 
    res_json = json.dumps(res, ensure_ascii=False)
    
    return res_json 
    # return render_template('naver.html', movies=res_json)


if __name__ == '__main__':
    app.run('localhost', port='8585')
