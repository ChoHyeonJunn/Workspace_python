# -*- coding:utf-8 -*-


def fibo1(num):
    a, b = 0, 1
     
    for i in range(num):
        print('fibo num {} = {}'.format(i, a))
        a, b = b, a + b


lst = list()


def fibo2(num):
    a, b = 0, 1

    for i in range(num):    
        lst.append(a)
        a, b = b, a + b
        
        
if __name__ == '__main__':
    fibo1(int(input('fibo1 입력 : ')))
    fibo2(int(input('fibo2 입력 : ')))
    print(lst)
