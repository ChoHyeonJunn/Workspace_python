# -*- coding:utf-8 -*-

# pip install flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask"

if __name__ == '__main__':
    app.run()
    # Ctrl + C 종료는 cmd 창에서 가능한것 이클립스에서는 그냥 버튼으로 종료!