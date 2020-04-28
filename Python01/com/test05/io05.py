# -*- coding:utf-8 -*-

import pickle

score = {'name':'kh', 'kor':10, 'eng':40, 'math':60}

with open('test02.txt', 'wb') as file:
    pickle.dump(score, file)

'''
pickling : 객체 -> 파일에 저장
unpickling : 파일 -> 객체로 떼어온다
'''
    
