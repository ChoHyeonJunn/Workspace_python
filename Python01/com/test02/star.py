# -*- coding:utf-8 -*-

print('--------1.')
for i in range(5):
    print('*' * (i + 1))

print('--------1. join')
print('\n'.join([''.join(['*' for i in range(i + 1)]) for i in range(5)]))

print('--------2.')
for i in range(5, 0, -1):
    print('*' * (i))

print('--------2. join')
print('\n'.join([''.join(['*' for i in range(i)]) for i in range(5, 0, -1)]))

print('--------3.')
for i in range(0, 5):
    print(' ' * (4 - i), '*' * (i + 1))

print('--------3. join')
print('\n'.join([''.join([' ' for i in range(i)] + ['*' for i in range(6 - i)]) for i in range(5, 0, -1)]))

print('--------4.')
for i in range(0, 5):
    print(' ' * (i), '*' * (5 - i))

print('--------4.join')
print('\n'.join([''.join([' ' for i in range(5 - i)] + ['*' for i in range(i)]) for i in range(5, 0, -1)]))
    
print('--------5.')
for i in range(0, 5):
    print(' ' * (4 - i), '*' * ((i + 1) * 2 - 1))
    
print('--------5.join')
print('\n'.join([''.join([' ' for i in range(i)] + ['*' for i in range((6 - i) * 2 - 1)]) for i in range(5, 0, -1)]))

# print('-------- using join')
# 
# star = []
# space = [' ', ' ', ' ', ' ', ' ']
# 
# for i in range(0, 5):
#     star.append('*')
#     print(''.join(star))
# 
# print('--------')
# 
# for i in range(5, 0, -1):
#     print(''.join(star))
#     star.pop(i - 1)
# 
# print('--------')
# 
# for i in range(0, 5):
#     star.append('*')
#     space.pop(4 - i)
#     print(''.join(space), ''.join(star))
# 
# print('--------')
# 
# for i in range(0, 5):
#     print(''.join(space), ''.join(star))
#     space.append(' ')
#     star.pop(4 - i)
# 
# print('--------')
# 
# star.append('*')
# for i in range(0, 5):
#     space.pop(4 - i)
#     print(''.join(space), ''.join(star))
#     star.append('*')
#     star.append('*')
