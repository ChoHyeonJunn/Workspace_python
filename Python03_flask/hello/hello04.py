# -*- coding:utf-8 -*-

# 같은 모듈 (여기서는 flask) 안에 있는 모듈은 컴마로 구분해서 임포트하는것을 허용, 같은 모듈이 아니라면 가능은 하지만 권장하지 않음!! 보기안좋아새기야
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_root():
    html = '''
        <h1>GET/POST</h1>
        
        <a href="/test">get</a><br>
        
        <form action = "/test" method="post">
            <input type="submit" value="post"/>
        </form>
    '''
    
    return html


@app.route('/test', methods=['GET', 'POST'])
def hello_test():
    if request.method == 'POST':
        html = '''
            <h1 style="color:red">POST</h1>
        '''
    else:
        html = '''
            <h1 style="color:blue">GET</h1>
        '''
    return html


if __name__ == '__main__':
    app.run()
