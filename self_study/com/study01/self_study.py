# -*- coding:utf-8 -*-
from matplotlib._image import resample

# n = input()
# 
# for i in range(1, int(n) + 1):
#     for j in range(1, int(n) + 1):
#         if int(i) + int(j) >= int(n) + 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     else:
#         print()
# while 1:
#     a, b = input().split(' ')
#     
#     if(int(a) == 0 & int(b) == 0):
#         break
#     else:
#         print(int(a) + int(b))
# num = int(input())
# a, b = num // 10, num % 10
# count = 0
# 
# while True:
#     count += 1
#     a, b = b, (a + b) % 10
#     if a == (num // 10):
#         if b == (num % 10):
#             break
# print(count)
# score = 0
# i = 0
# while i < 5:
#     num = int(input())
#     
#     if num < 40:
#         score += 40
#     else:
#         score += num
#     
#     i += 1
# 
# print(score // 5)
# x = int(input())
# y = int(input())
# 
# if x > 0:
#     if y > 0:
#         print(1)
#     else:
#         print(4)
# else:
#     if y > 0:
#         print(2)
#     else:
#         print(3)
# a = int(input())
# b = int(input())
# c = int(input())
# x = int(input())
# y = int(input())
# 
# MIN = lambda x, y:x if x < y else y
# print(MIN(a, MIN(b, c)) + MIN(x, y) - 50)
# a, b, c = input().split(' ')
# a, b, c = int(a), int(b), int(c)
# 
# if b >= c:
#     print(-1)
# else:
#     count = a // (c - b)
#     print(count + 1)
# def solve(a: list):
#     result = 0
#     for i in a:
#         result += i 
#     
#     return result
# def factorial(n, res):
#     if n == 0:
#         return res
#     
#     res *= n
#     
#     return factorial(n - 1, res)
# 
# 
# if __name__ == '__main__':
#     n = int(input())
#     print(factorial(n, 1))
# def fibo(n, cache=dict()):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     
#     if n in cache:
#         return cache[n]
#     
#     cache[n] = fibo(n - 1, cache) + fibo(n - 2, cache)
#     
#     return fibo(n - 1, cache) + fibo(n - 2, cache)
# 
# 
# if __name__ == '__main__':
#     n = int(input())
#     print(fibo(n))

star = list()


def setStar(N):
    if N == 3:
        for i in range(N):    
            for j in range(N):
                if j >= N / 3 and j < (N / 3) * 2 and i >= N / 3 and i < (N / 3) * 2:
                    star[i][j] = ' '
                else:
                    star[i][j] = '*'
    
    return setStar(N / 3)


if __name__ == '__main__':
    N = int(input())
    
    star = [['' for j in range(N)] for i in range(N)]
    
    setStar(N)
    for i in range(N):
        for j in range(N):
            print(star[i][j], end='')
        print()




