'''
题目：利用循环打印菱形
'''

SIZE = 5
SHOW = ' *'
HIDE = '  '

# 坐标系构建法
for y in range(SIZE - 1, -SIZE, -1):
    for x in range(-SIZE + 1, SIZE, 1):
        if (y > x - SIZE) and (y < x + SIZE) and \
                (y > -x - SIZE) and (y < -x + SIZE):
            print(SHOW, end='')
        else:
            print(HIDE, end='')
    print()
