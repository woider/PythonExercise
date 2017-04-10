'''
题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
'''

import math

for i in range(10000):
    n = math.sqrt(i + 100)
    m = math.sqrt(i + 268)
    if n % 1 == 0 and m % 1 == 0:
        print(i)
