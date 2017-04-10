'''
题目：格式化输出当前时间。
'''

import time

format = '%Y-%m-%d %H:%M:%S'
local = time.localtime(time.time())

print(time.strftime(format, local))
