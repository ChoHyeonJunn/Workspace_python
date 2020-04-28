# -*- coding:utf-8 -*-

# 1. for문을 사용하여 구구단 전체를 출력하는 gugu()함수를 만들자.
# 2. while 문을 사용하여 입력된 숫자의 단만 출력하는 gugudan(x)함수를 만들자.
# 3. main 만들어서 위의 두 함수를 호출하자


def gugu():
    for i in range(2, 10):
        print('<', i, '단>')
        for j in range(1, 10):
            print(i, '*', j, '=', i * j, end='\t')
        else:
            print()


def gugudan(x):
    i = 1
    print('<', x, '단>')
    while i <= 9:
        print(x, '*', i, '=', x * i, end='\t')
        i += 1


if __name__ == '__main__':
    gugu()
    gugudan(int(input('원하는 단 수 입력 : ')))
