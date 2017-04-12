'''
编程找出1000以内的所有完数。
'''

RAN = 1000  # 完数范围

for i in range(2, RAN + 1):
    l = []  # 因数列表
    for j in range(1, i):
        if (i % j) == 0:
            l.append(j)
    if sum(l) == i:
        print(i, ':', l)
