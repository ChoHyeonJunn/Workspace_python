# -*- coding:utf-8 -*-

subject = ['java', 'javascript', 'python']
for i in subject:
    print(i)

for i in subject:
    print(i, end=' ')
else:
    print('\n재밌다.')  # 반복문이 정상적으로 완료된 이후에 else에 있는 명령문 수행

for i in range(1, 100):
    print(i, end=',')
else:
    print(100)
    
print('--------')
print('<<구구단>>')
for i in range(2, 10):
    print("< " + str(i) + "단 >")
    
    for j in range(1, 10):
        print(i , "*" , j , "=" , (i * j), sep=' ', end='\t')
    else:
        print()
    
print('--------') 
print('10 ~ 1')   
for i in range(10, 0, -1):
    print(i, sep=' ', end=' ')
    
