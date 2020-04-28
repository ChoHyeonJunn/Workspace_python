# -*- coding:utf-8 -*-

# pip install Jinja2 
# Jinja2 는 flask install 하며 자동으로 같이 install 된다!

# application : Contoller 역할을 하는 부분이다!
# templates : html 파일들이 들어간다.
# static : css , js 등이 들어간다.

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return '''
        <a href="/hello">hello</a>
        <input type="button" value="hello" onclick="location.href='/hello/name'"/>
    '''

    
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/test', methods=['post'])
def test():
    return render_template('test.html', test=request.form['command'])


if __name__ == '__main__':
    app.run('localhost', port='8585')
