# -*- coding:utf-8 -*-

# input() 함수
# n = input('n 입력 :')

# 피보나치 수열

# a, b = 0, 1
# i = 0
# 
# while i < int(n):
#     print(a, end=' ')
#     a, b = b, a + b
#     i += 1
# print()

        
def fibo(x):
    a, b = 0, 1
    
    for i in range(x):
        print('fibo {} = {}'.format(i, a))
        a, b = b, a + b
    
    return 'fibo {} = {}'.format(x, a)
    
    
if __name__ == '__main__':
    print(fibo(int(input('fibo num : '))))
