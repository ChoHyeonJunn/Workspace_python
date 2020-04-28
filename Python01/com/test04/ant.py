# -*- coding:utf-8 -*-

# 개미수열
# def ant(antList):
#     newList = []
#         
#     temp = antList[0]
#     count = 1
#     
#     for i in range(1, len(antList)):
#         if int(antList[i]) != temp:
#             newList.append(count)
#             newList.append(temp)
#             
#             temp, count = antList[i], 1
#         else:
#             temp, count = antList[i], count + 1
#     else:
#         newList.append(count)
#         newList.append(temp)
#     
#     return newList
# 
# 
# if __name__ == '__main__':
#     n = int(input('ant stage : '))
#     val = ant([1])
#     
#     print([1])
#     for i in range(1, n):
#         val = ant(val)
#         print(val)
        
        
# teacher

def ant(i):
    inp = str(i)
    cnt = 0
    target = inp[0]
    res = ''
    for a in inp:
        if a == target:
            cnt += 1
        else:
            res+= target + str(cnt)
            cnt = 1
            target = a
            
    res += target + str(cnt)
    return res

if __name__ == '__main__':
    n = int(input('ant stage : '))
    val = ant(1)
     
    print('1')
    print(val)
    for i in range(1, n):
        val = ant(val)
        print(val)