# -*- coding:utf-8 -*-

# cmd 창에서...
# pip install numpy         -> 수치 해석 (머신러닝, 딥러닝 등에 많이 쓰임)
# pip install matplotlib    -> 그래프 그리는 lib
# WARNING 시 ... python -m pip install --upgrade pip

import numpy as np
import matplotlib.pyplot as plt
import random
from unicodedata import category


def plt01():
    x = np.arange(0, 11)
    y = x
    
    plt.plot(x, y)
    
    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend(['y = x'])
    
    plt.show()


def plt02():
    y = [random.randint(0, 10) for i in range(10)]
    x = range(10)
    
    plt.bar(x, y)
    
    plt.xticks(range(11))
    plt.yticks(range(11))
    
    plt.show()


def plt03():
    data = [random.randint(100, 1000) for i in range(4)]
    
    plt.pie(data)
    
    category = ['first', 'second', 'third', 'fourth']
    plt.legend(category)
    
    plt.show()


if __name__ == '__main__':
    plt01()
    plt02()
    plt03()