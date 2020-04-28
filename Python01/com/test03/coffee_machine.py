# -*- coding:utf-8 -*-


def coffee(count, money):
    # 잔돈 계산
    change = money - (100 * count)
    # prn 호출(커피 잔 수, 잔돈)
    if change >= 0:
        prn(count, change)
    else:
        prn()  # python에서는 함수호출시 파람을 넘겨주지않으면 초기화된 값으로 입력된다.


def prn(count=0, change=0):
    # 출력 (커피 몇 잔이 나왔습니다. 잔돈은 얼마 입니다.)(돈이 부족합니다.)
    if count == 0 & change == 0:
        print('돈이 부족합니다.')
    else:
        print('커피 {} 잔이 나왔습니다. 잔돈은 {} 원 입니다.'.format(count, change))


def start():
    # 커피 잔 수 입력
    count = int(input('커피 잔 수 입력 : '))
    # 돈 입력
    money = int(input('돈 입력(한잔에 100원) : '))
    # coffee 함수에 잔수와 돈 전달하면서 호출
    coffee(count, money)


if __name__ == '__main__':
    start()
