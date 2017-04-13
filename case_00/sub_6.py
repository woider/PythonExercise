'''
题目：斐波那契数列。
'''

arr = [0, 1]

tmp, num = 0, 1

dep = 20  # 数列长度

for i in range(dep - 2):
    tmp, num = num, tmp + num
    arr.append(num)

print(arr)
