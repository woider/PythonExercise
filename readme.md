Python3 练习题 100例
====================


## [题目 1](https://github.com/woider/PythonExercise/blob/master/case_10/sub_1.py) ##

有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

> 可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。


## [题目 2](https://github.com/woider/PythonExercise/blob/master/case_10/sub_2.py) ##

企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

> 请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。


## [题目 3](https://github.com/woider/PythonExercise/blob/master/case_10/sub_3.py) ##

一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

> 在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。


## [题目 4](https://github.com/woider/PythonExercise/blob/master/case_10/sub_4.py) ##

输入某年某月某日，判断这一天是这一年的第几天？

> 以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天。


## [题目 5](https://github.com/woider/PythonExercise/blob/master/case_10/sub_5.py) ##

输入三个整数x,y,z，请把这三个数由小到大输出。

> 我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。


## [题目 6](https://github.com/woider/PythonExercise/blob/master/case_10/sub_6.py) ##

斐波那契数列。

> 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。


## [题目 7](https://github.com/woider/PythonExercise/blob/master/case_10/sub_7.py) ##

将一个列表的数据复制到另一个列表中。

> 使用列表[:]。


## [题目 8](https://github.com/woider/PythonExercise/blob/master/case_10/sub_8.py) ##

输出 9*9 乘法口诀表。

> 分行与列考虑，共9行9列，i控制行，j控制列。


## [题目 9](https://github.com/woider/PythonExercise/blob/master/case_10/sub_9.py) ##

模拟Linux用户登录。

> 验证账号和密码，若失败则延迟三秒输出错误信息。


## [题目 10](https://github.com/woider/PythonExercise/blob/master/case_10/sub_10.py) ##

格式化输出当前时间。

> 使用 time 模块，格式为 yyyy-mm-dd HH:mm:ss。