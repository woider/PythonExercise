'''
题目：输出指定格式的日期。
'''

import datetime

# 日期格式
form = '%Y-%m-%d'

# 日期对象
date1 = datetime.date(1945, 8, 15)
print('抗战胜利：', date1.strftime(form))

# 日期运算
date2 = date1 + datetime.timedelta(days=18)
print('二战结束：', date2.strftime(form))

# 日期替换
date3 = date2.replace(year=1949, month=10, day=1)
print('开国大典：', date3.strftime(form))

# 当前日期
date4 = datetime.date.today()
print('当前日期：', date4.strftime(form))
