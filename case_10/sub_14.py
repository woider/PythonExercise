'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''

num = int(input('input num: '))
arr = []  # 质因数列表

tmp = num
while tmp != 1:
    pri = 2
    while pri != (num + 1):
        if (tmp % pri) == 0:
            tmp = tmp // pri
            arr.append(pri)
        else:
            pri += 1

exp = ' * '.join(map(str, arr))
print('%d = %s' % (num, exp))
