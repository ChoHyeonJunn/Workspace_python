# -*- coding:utf-8 -*-

# import math
# math라는 module ( = library) 가져온다.

from math import pi
# math module 의 pi만 가져온다.


def circle(x):
    return x * x * pi


if __name__ == '__main__':
    x = int(input('원의 반지름 : '))
    print('반지름이 {}인 원의 넓이는 {} 입니다.'.format(x, circle(x)))

