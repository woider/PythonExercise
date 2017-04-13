'''
题目：一个5位数，判断它是不是回文数。
'''

num = str(int(input('输入数字：')))

# 判断是否为回文
def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


print('是否为回文数：', palindrome(num))
