# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)

db = client.test
score = db.score

cursor = score.find()  # 한개인지 여러개인지 모르고 Cursor Object로 리턴한다
for doc in cursor:
    pprint.pprint(doc)

print('--------------------------')
hong = score.find({'name': '홍길동'})
for doc in hong:
    pprint.pprint(doc)
    
print('--------------------------')
cho = score.find_one({'name': '조세호'})  # find_one cursor 객체로 리턴되지않음. 하나만 찾아 값 자체로 리턴
pprint.pprint(cho)

print('--------------------------')
print('document 의 총 개수', score.count_documents({}))

print('--------------------------')
# 국어점수가 70점보다 높은 document
kor = score.find({'kor': {'$gt': 70}})
for doc in kor:
    print(doc)
    
    
