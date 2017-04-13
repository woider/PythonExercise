'''
题目：给一个不多于5位的正整数
要求：一、求它是几位数，二、逆序打印出各位数字。
'''

num = int(input('正整数：'))

arr = []  # num 的每一位

while num != 0:
    arr.insert(0, str(num % 10))
    num = num // 10

print('%s 为 %d 位数' % (''.join(arr), len(arr)))

arr.reverse()  # 反向列表中元素

print('倒序输出', ''.join(arr))
