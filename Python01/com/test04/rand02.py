# -*- coding:utf-8 -*-

import random as r

lot = set()


def lotto():
    lotto = set()
    
    while len(lotto) <= 6:
        ran = r.randint(1, 45)
        lotto.add(ran)
    print(list(lotto))
    
    lst = sorted(lotto)  # 자동 정렬해서 리스트로 리턴
    print(lst)


if __name__ == '__main__':
    lotto()
