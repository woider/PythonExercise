'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''


def reverse(str):
    if len(str) == 0:
        return str
    return reverse(str[1:]) + str[0]


poetry = input('五言绝句：')
print(reverse(poetry))
