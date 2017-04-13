'''
题目：求1+2!+3!+...+20!的和。
'''

from math import factorial

arr = []  # 阶乘列表

for i in range(1, 21):
    arr.append(factorial(i))

exp = '1! + 2! + 3! + ... + 20!'
print('{0} = {1}'.format(exp, sum(arr)))
