'''
题目：输出 9*9 乘法口诀表。
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        exp = '%d * %d = %d' % (i, j, i * j)
        print(exp, end='\t')
    print()
