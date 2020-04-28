# 산술연산

a = 21
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a ** b)  # a^b 거듭제곱
print(a // b)  # 몫 (floor devision)
print(a % b)  # 나머지

# 비교연산
a, b = 5, 3
print(a == b)
print(a != b)
print(a > b)
print(a <= b)

print(a is b)
print(a is not b)

print(True or False)
print(False and True)
print(not False)

# 범위연산
list01 = list(range(100))  # 0 ~ (n-1)
print(list01)
print(list01[2])
print(list01[12:49])
print(list01[12:49:3])

# [start:end] -> start ~ end-1
# [start:end:step] -> start, start+step, ... end-1

# Hello 만 출력
str01 = 'Hello, World!'
print(str01[0:5])
print(str01[7:])  # 안써주면 끝까지 갑니다~!

# reverse
print(str01[-1])
print(str01[::-1])

# 멤버 연산
list02 = [0, 1, 2, 3, 4]
print(3 in list02)
print(5 not in list02)
print(4 not in list02)














