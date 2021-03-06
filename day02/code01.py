#__author__ = "linnum"
#__time__ = "2019/11/18 7:01 AM"

'''
    数据类型
'''

# 整数
# -- 十进制
num01 = 18
# -- 二进制
num02 = 0b11
print(num02)  # 输出结果会按十进制

# -- 八进制(逢八进一)  0 1...7   10  11  12 ......
num03 = 0o10
print(num03)

# -- 十六进制(逢16进1)  0--9  a--f
num04 =  0x10
print(num04)

# 小整数对象池    CPython中 -5--256存储在对象中，可以重复使用
a = 1000
b = 1000
# 在交互式中，两个1000不是同一个对象
print(id(a))
print(id(b))