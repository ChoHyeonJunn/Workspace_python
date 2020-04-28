# -*- coding:utf-8 -*-


# 함수나 클래스는 끝난 후에 2줄 공백을 권장
def func01():
    pass  # 함수에 내용이 아무것도 없다면 pass 라는 키워드 사용


def func02():
    print('함수 02 입니다.')


def func03():
    return '함수 03 입니다.'
    

def func04():
    return {1:'a', 2:200}
    
        
if __name__ == '__main__':
    # main : 프로그램의 주 진입점
    func02()
    print(func02())  # None == null
    str01 = func03()
    print(str01)
    print(func04()[1])  # dictionary 의 key 1을 통해 값을 가져옴
    
