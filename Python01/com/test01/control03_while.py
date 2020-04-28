# -*- coding:utf-8 -*-

i = 1
while i <= 10:
    print(i)
    i += 1
    # python 에는 ++ -- 연산자 없음!!

print('------------- 1~10 까지 합 ----------------')
mysum = 0
mycount = 1
while mycount <= 10:
    mysum += mycount
    mycount += 1
else:
    print('mysum', mysum, sep=':')
    print('mycount', mycount, sep=':')
