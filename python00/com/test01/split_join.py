# split
str01 = 'Hello, World!\nHello, Python!'
print(str01)

arr01 = str01.split(' ')
print(arr01)

arr02 = str01.split(' ', 1)  # 1번만 자름
print(arr02)

import re

arr03 = re.split('[\s]|[,]', str01)
print(arr03)

# join
arr04 = ['1', '2', '3', '4']
print(arr04)
print('+'.join(arr04))

print(eval('+'.join(arr04)))