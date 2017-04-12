'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''

from math import sqrt

min = 101
max = 200

prime = list()

for i in range(min, max + 1):
    temp = int(sqrt(i))
    flag = True  # 是否为素数
    for j in range(2, temp + 1):
        if (i % j) == 0:
            flag = False
            break
    if flag == True:
        prime.append(i)

print('%d-%d 之间共有 %d 个素数' % (min, max, len(prime)))
print(prime)
