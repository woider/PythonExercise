'''
题目：输入某年某月某日（yyyy-MM-dd），判断这一天是这一年的第几天？
'''

cal = input('日期：')

date = cal.split('-')  # 拆分日期

year = int(date[0])
month = int(date[1])
day = int(date[2])

arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num = 0

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    arr[2] = 29

for i in range(1, len(arr)):
    if month > i:
        num += arr[i]
    else:
        num += day
        break

print('天数：', num)
