# -*- coding: cp949 -*-

import random

a = random.randrange(0, 31)
b = random.randrange(0, 101)
c = random.randrange(500, 1001)

x = 0
while 1:
    option, choose = map(int, input().split())

    x += 1
    target = (a * x + b) % c

    if option == 1:     # 낮은지
        if target > choose:
            print(True)
        else:
            print(False)
    elif option == 2:   # 같은지
        if target== choose:
            print(True)
        else:
            print(False)
    elif option == 3:   # 높은지
        if target < choose:
            print(True)
        else:
            print(False)