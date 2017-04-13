'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''


class Code:
    content = ''  # 代码
    letters = 0  # 字母
    space = 0  # 空格
    digit = 0  # 数字
    others = 0  # 字符

    # 构造函数
    def __init__(self, content):
        self.content = content

    # 分析代码
    def analysis(self):
        for c in self.content:
            if c.isalpha():
                self.letters += 1
            elif c.isspace():
                self.space += 1
            elif c.isdigit():
                self.digit += 1
            else:
                self.others += 1

    # 展示结果
    def showData(self):
        form = '字母（%d） 空格（%d） 数字（%d） 其他字符（%d）'
        data = (self.letters, self.space, self.digit, self.others)
        print(form % data)


content = input('请输入一段代码：\n')

code = Code(content)
code.analysis()  # 分析
code.showData()  # 展示
