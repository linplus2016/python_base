#__author__ = "linnum"
#__time__ = "2020/1/28 10:34 AM"

# 练习一 闰年判断

year = int(input("请输入年份： "))
result =  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(result)

# 练习二 4位整数，求4位相加之和

num = int(input("请输入一个4位的整数： "))

# 自己的方法
first_num = num % 10
second_num = (num % 100 - first_num)/10
third_num = (num % 1000 - second_num*10 - first_num)/100
forth_num = (num % 10000 - third_num*100 - second_num*10 - first_num )/1000
result_2 = first_num + second_num + third_num + forth_num

# 老师的方法 使用//代替了我写的部分计算公式，更加简化
unit01 = num  % 10
unit02 = num // 10 % 10
unit03 = num // 100 % 10
unit04 = num // 1000 % 10
# 老师的方法2
result_3 = num % 10
result_3 += num // 10 % 10
result_3 += num // 100 % 10
result_3 += num // 1000

print(int(first_num))
print(int(second_num))
print(int(third_num))
print(int(forth_num))
print(int(result_2))
print(unit01)
print(unit02)
print(unit03)
print(unit04)
print(unit01 + unit02 + unit03 + unit04)
print(result_3)

# 练习3  获取总秒数，计算几时几分几秒

time = int(input("请输入总秒数： "))
second = time % 60
minute =  time // 60
hour = time // 3600
print('%d 小时 %d 分 %d 秒' %( hour, minute, second))
print(type(hour))

# 练习3  奇偶数判断

int_num = int(input("请输入一个整数： "))
if int_num % 2 == 0:
    print("这是一个偶数")
else :
    print("这是一个奇数")


