'''
题目：利用递归方法求5!。
'''


def factor(n):
    if not isinstance(n, (int)):
        raise TypeError()
    if n < 1:
        raise Exception()
    if n == 1:
        return 1
    return factor(n - 1) * n


n = 5

print('%d! = %d' % (n, factor(n)))
