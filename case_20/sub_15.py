'''
题目：利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''

score = int(input('输入成绩：'))
rank = None

if 0 <= score and score < 60:
    rank = 'C'
elif 60 <= score and score < 90:
    rank = 'B'
elif 90 <= score and score <= 100:
    rank = 'A'

if rank != None:
    print('%d 属于等级 %s' % (score, rank))
else:
    print('成绩应在 0-100 之间')
