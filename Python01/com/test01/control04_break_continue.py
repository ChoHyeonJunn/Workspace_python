# -*- coding:utf-8 -*-

i = 1
while i <= 10:
    if i > 5:
        print('break!')
        break;
    print(i)
    i += 1
else:
    print('i:', i)  # break 로 인해 while문이 정상적으로 종료되지 않아 실행되지않음!

#

for i in range(1, 10):
    if i % 2:
        continue
    print(i)
else:
    print('i', i, sep=':')

#

