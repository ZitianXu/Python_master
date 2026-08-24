"""
    这是一个用来测试的文件
"""

import time

# 打印一个整型字面量
print(666)
"""
    多行注释
    下面是
    浮点数和字符串 
    
"""
print(13.14)

print("你好世界")



#变量
money = 999

print("钱包还有:", money)

money -= 10

print("钱包还有:", money)

# 类型
print(type(666))
print(type(13.14))
print(type("你好世界"))
money_type = type(money)
print(money_type)

# 数字转字符串
num_str = str(99)
print(type(num_str), num_str)

float_str = str(11.345)
print(type(float_str), float_str)

# 字符串转数字
num_str = int("987")
print(type(num_str), num_str)

# 字符串转浮点
float_str = float("11.2334")
print(type(float_str), float_str)

# 浮点数转整型:丢失精度
num_float = int(11.567)
print(type(num_float), num_float)

# 幂运算
num = 3
num **= 3
print(num)

# 整除
num //= 2
print(num)

name = '我是谁'
print(type(name))

name = "我是谁"
print(type(name))

name = """
我
是
谁
"""
print(type(name))

name = '"我是谁啊"'
print(name)

# 转义字符
name = "\"我是你你是我\""
print(name)

name = '\"我是你你是我\"'
print(name)

name = "\'我是你你是我\'"
print(name)

# 字符串拼接
print("我是" + name + "什么玩意")

# 字符串格式化
name = "我是乐乐"
message = "哈哈 %s" % name
print(message)

num = 12345
salary = 54321
message = "我的学号是%s, 我的薪资是%s" % (num, salary)
print(message)

average_salary = 12345.66
message = "我的学号是%s, 我这个月的薪资是%d, 我去年的平均薪资是%f" % (num, salary, average_salary)
print(message)

# 格式化精度控制
num1 = 11
num2 = 11.635
print("数字11宽度限制5, 结果是:%5d" % num1)
print("数字11宽度限制1, 结果是:%1d" % num1)
print("数字11.635精度限制2, 结果是:%.2f" % num2)
print("数字11.635宽度限制7, 精度限制2, 结果是:%7.2f" % num2)

# 字符串快速格式化
name = "徐大牛"
num = 1024
stick_price = 1.99
print(f"我的名字是{name},我的学号是{num}, 一包辣条{stick_price}。")

# 对表达式进行格式化
print("1*1的结果是: %d" % (1 * 1))
print(f"1*1的结果是: {1 * 1}")
print("字符串在Python中的类型是: %s" % type('字符串'))

# 数据输入(input)
""" 
print("请告诉我你是谁: ")
name = input()
"""

"""
name = input("请告诉我你是谁: ")
print("你的名字是%s" % name)
"""

"""
num = input("请告诉我你的银行卡密码: ")
数据类型转换(input函数默认输入字符串)
num = int(num)
print("你的密码格式是: ", type(num))
"""

#比较运算符
result = "athletic" == "ethic"
print(f"比较结果为: {result}, 类型是:{type(result)}")

num1 = 10
num2 = 10
print(f"10 == 10 比较的结果是: {num1 == num2}")


# 判断语句
age = 30
print(f"我今年{age}岁了")
if age >= 18:
    print("我已经成年了")

# if else 组合判断语句

# print("欢迎来到游乐园，儿童免费,成人收费")
# age = int(input("请输入你的年龄:"))
# if age >= 18:
#     print("您已成年，请缴费")
# else:
#     print("您未成年，玩的开心")



# if elif else组合使用


# height = int(input("请输入你的身高: "))
# vip_level = int(input("请输入你的VIP等级: "))
# day = int(input("请告诉我今天是几号: "))

# if height<=120:
#     print("身高低于120cm, 可以免费。")
# elif vip_level >= 3:
#     print("尊敬的会员大人，您免费了。")
# elif day == 1:
#     print("今天福利日，免费了。")
# else:
#     print("收成人票。")



# if int(input("请输入你的身高: ")) <= 120:
#     print("身高不到一米二，免费")
# elif int(input("请输入你的VIP等级: ")) >=5:
#     print("尊敬的会员大人，您免费了。")
# elif int(input("请告诉我今天是几号: ")) == 1:
#     print("今天福利日，免费了。")
# else:
#     print("收成人票。")



# 判断语句嵌套使用

# if int(input("你的身高是多少")) >= 120:
#     print("身高超出限制，不可以免费")
#     print("但是如果vip等级大于3，可以免费")

#     if int(input("你的vip等级是多少: ")) >= 3:
#         print("恭喜你，你可以免费了")
#     else:
#         print("你要付钱的")    
# else:
#     print("你的身高小于120cm, 可以免费")



# 案例：猜数字

# import random
# num = random.randint(1,10)

# guess_num = int(input("输入你要猜测的数字: "))

# if guess_num == num:
#     print("猜对啦")
# else:
#     if guess_num < num:
#         print("小了")
#     else:
#         print("大了")

#     guess_num = int(input("再试试看吧："))

#     if guess_num == num:
#         print("猜对啦")
#     else:
#         if guess_num < num:
#                 print("小了")
#         else:
#                 print("大了")

#         guess_num == int(input("最后再来一遍: "))
#         if guess_num == num:
#                 print("猜对啦")
#         else:
#                 print(f"可惜了，正确的数字是{num}")



# while循环猜数字

# import random
# num = random.randint(1,100)
# flag = True
# count = 0

# while flag:
#     guess_num = int(input("请输入你的数字: "))
#     count += 1
#     if guess_num == num:
#         flag = False
#         print("恭喜你猜对了!")
#     elif guess_num < num:
#         print("小了")
#     else:
#         print("大了")

# print(f"你一共猜了{count}次")



# while嵌套

i = 1
while i <= 5:
    print(f"今天是第{i}天，准备表白")

    j = 1
    while j <= 6:
        print(f"送给小美第{j}支玫瑰花")
        j += 1
    print("小美我喜欢你")
    i += 1


# for循环遍历字符串

name = "Andy"
for i in name:
    print(i)



# 数有多少个a

sentence = "AaaaA!"
count = 0
for i in sentence:
    if i == "A" or i == "a":
        count += 1
print(f"{sentence}里面一共有{count}个a字母")
    

# range语法1

# for x in range(10):
#     print(x)



# range语法2

# for x in range(5,10):
#     print(x)



# range语法3

# for x in range(5,10,2):
#     print(x)
    


# for循环临时变量作用域

# i = 0
# for i in range(5):
#     print(i)
# print (i)


# for循环嵌套

# for i in range(101):
#     for j in range(10):
#         print(f"今天是第{i}天, 送了{j}朵玫瑰花")

# print(f"今天是第{i}天, 表白成功了")



# for循环打印99乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i}= {j * i}\t", end='')
    print()



# continue

# for i in range(1,5):
#     print("1")
#     continue
#     print(2)




# continue嵌套

# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")



# break

# for i in range(1,101):
#     print("语句1")
#     break
#     print("语句2")

# print("语句3")



# break嵌套

# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         break
#         print("语句3")

#     print("语句4")





# 函数

def my_length(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

str1 = "xzt12345"
my_length(str1)


# 函数的调用

def welcome():
    print("欢迎光临！")

welcome()

# 函数传参

def add(x, y):
    result = x + y
    print(f"{x}+{y}的计算结果是: {result}")

add(1, 2)


# 函数测体温

def check(num):
    print("欢迎你！请测量体温")
    if num <= 37.5:
        print(f"您的体温为{num}正常，进去吧")
    else:
        print(f"你的体温达到了{num}摄氏度, 请做核酸检测")


check(38.1)



# 函数返回值

def add(x,y):
    result = x + y
    return result
    # 返回结果后，还想输出一句话，打不出来的
    print("我完事了")

r = add(1,5)
print(r)


# None返回值

def say_hi():
    print("你好呀")

result = say_hi()
print(f"无返回值函数，结果是{result}")
print(f"无返回值函数，结果类型是{type(result)}")


# 主动返回None

def say_hi2():
    print("你好呀")
    return None

result = say_hi2()
print(f"无返回值函数，结果是{result}")
print(f"无返回值函数，结果类型是{type(result)}")


# None用于if判断

def check_age(age):
    if age > 18:
        return("SUCCESS")
    else:
        return None

result = check_age(15)
if not result:
    print("年龄未满，不得进入")


# None用于声明无初始内容的变量
name = None


# 对函数进行文档说明

def add(x, y):
    """
    123456
    """

    result = x + y


# 演示局部变量

# def test_a():
#     num = 100
#     print(num)

# test_a()
# # 出了函数体，局部变量无法使用
# print(num)


# 演示全局变量

num = 100
def test_a():
    print(num)

def test_b():
    num = 200
    print(num)

test_a()
test_b()
print(num)



# 使用global变成全局变量
num = 100
def test_a():
    print(num)

def test_b():
    global num 
    num = 200
    print(num)

test_a()
test_b()
print(num)





# 函数综合案例: ATM

# money = 5000000
# name = None

# name = input("请输入你的姓名: ")


# # 查询函数

# def query(show_header):
#     if(show_header):
#         print("-----------------查询余额-----------------")
    
#     print(f"{name}, 您好! 您当前的余额是: {money}元")


# # 存款函数
# def save_money(num):
#     global money
#     money += num
#     print("-----------------存款-----------------")
#     print(f"{name}, 您好! 你这次存了{num}元")

#     # 调用query函数查询余额但不打印标题
#     query(False)

# # 取款函数
# def get_money(num):
#     global money
#     money -= num
#     print("-----------------取款-----------------")
#     print(f"{name}, 您好! 你这次取了{num}元")

#     # 调用query函数查询余额但不打印标题
#     query(False)

# # 主菜单函数
# def main():
#     print("-----------------主菜单-----------------")
#     print(f"{name}, 欢迎来到银行! 请选择你要办理的业务:") 
#     print("查询余额\t[输入1]")   
#     print("存款\t\t[输入2]" )
#     print("取款\t\t[输入3]") 
#     print("退出\t\t[输入4]" )  # 通过制表符\t对齐输出
#     return input("请输入你的选择:")


# # 设置无限循环
# while True:
#     keyboard_input = main()
#     if keyboard_input == "1":
#         query(True)
#         continue   # 通过continue进入下一次循环
#     elif keyboard_input == "2":
#         num = int(input("你想要存多少钱? 请输入: "))
#         save_money(num)
#         continue
#     elif keyboard_input == "3":
#         num = int(input("你想要取多少钱? 请输入: "))
#         get_money(num)
#         continue
#     else:
#         print("程序退出啦")
#         break     # 通过break退出循环








# 数据容器

# 列表

name_list = ['Andy', 'Cai', 'Murat' ]
print(name_list)
print(type(name_list))


# 元素类型任意

my_list = ['Andy', 666, True]
print(my_list)
print(type(my_list))

# 嵌套列表

my_list = [[1,2,3], [4,5,6]]
print(my_list)
print(type(my_list))

# 列表下标（索引）

my_list = ['Andy', 666, False]
print(my_list[0])
print(my_list[1])
print(my_list[2])

# 反向索引

print(my_list[-1])
print(my_list[-2])
print(my_list[-3])


# 嵌套列表索引

my_list = [[1,2,3], [4,5,6]]
print(my_list)
print(my_list[0][0])
print(my_list[0][1])
print(my_list[1][0])
print(my_list[-1][-1])

# 列表查询

my_list = ['Andy', 67, 'Xu', True]
index = my_list.index('Andy')
print(f"Andy在mylist列表中的索引值是:{index}")
print(my_list)

# 修改元素

my_list[1] = 66
print(my_list)

# 插入元素

my_list.insert(1,666)
print(my_list)

# 追加元素

my_list.append(False)
print(my_list)

# 从其他数据容器追加元素

my_list_2 = [4,5,6]
my_list.extend(my_list_2)


my_list.extend([4,5,6])
print(my_list)

# 删除元素: del关键字
del my_list[2]
print(my_list)

# 删除元素: pop关键字, 能得到返回值传给变量
element = my_list.pop(1)
print(element)
print(my_list)

# 删除某元素在列表中第一个匹配项

my_list.remove(4)
print(my_list)

# 清除列表内容

my_list.clear()
print(my_list)

# 统计列表内某元素数量

my_list = ['Andy', 'Xu', True, False, 5, 6, 4, 5, 6]
count = my_list.count(5)
print(count)

# 统计列表里有多少元素

count = len(my_list)
print(count)




# 列表循环遍历


# while循环


def list_while_func():
    my_list = ["Andy", 666, True]

    # 定义一个变量表示下标
    
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(element)
        index += 1


list_while_func()

# for循环

def list_for_func():
    my_list = [1, 2, 3, 4, 5]
    for i in my_list:
        print(i)

list_for_func()


# 定义元组

t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()

print(f"t1的类型是:{type(t1)}, 内容是:{t1}")
print(f"t2的类型是:{type(t2)}, 内容是:{t2}")
print(f"t3的类型是:{type(t3)}, 内容是:{t3}")

# 单个元素后面要加逗号，保持元组类型
t4 = (520, )
print(f"t4的类型是:{type(t4)}, 内容是:{t4}")

# 元组的嵌套

t5 = (1, 2, 3, (4, 5))
print(f"t5的类型是:{type(t5)}, 内容是:{t5}")

# 下标索引取出内容
num = t5[3][1]
print(f"从数组t5里取出的内容是:{num}")


# index查找

t6 = ("Andy", "666", "Python")
index = t6.index("666")
print(f"'666'在t6中的下标是:{index}")

# count统计元素出现次数

t7 = ("Andy", "666", "666", "666", "Python")
count = t7.count("666")
print(f"在t7中, '666'一共出现了{count}次")

# len统计元素数量
t8 = ("Andy", "666", "666", "666", "Python", "Python", "Python", "Python")
num = len(t8)
print(f"t8里一共有{num}个元素")

# while遍历元组

index = 0
while index < len(t8):
    print(f"t8中的元素有: {t8[index]}")
    index+=1

# for遍历元组

for element in t8:
    print(f"t8中的元素有: {element}")

# 元组中列表内容可修改

t9 = (1, 2, 3, [4, 5, 6])
t9[3][0] = 6
print(t9)

# 字符串
my_str = "Andy is the best"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-10]
print(f"从my_str里分别取出下标为2和-10的元素, 值分别为{value}和{value2}")

# index
value = my_str.index("is")
print(f"在my_str中查找is, 他的起始位置是{value}")

# replace 方法
new_my_str = my_str.replace("best", "BEST")
print(new_my_str)

# split方法
my_str_list = my_str.split()
print(my_str_list)

# strip方法去首尾空格
my_str = "       Andy 6666666         "
my_str_strip = my_str.strip()
print(my_str_strip)

# strip去除首尾字符串
my_str = "12 Andy is 12 years old and he's turning 21"
my_str_strip2 = my_str.strip("12")
print(my_str_strip2)

# count统计其中某个字符串出现次数
my_str = "12121212"
count = my_str.count("12")
print(count)

# 统计字符串长度

num = len(my_str)
print(num)



# 序列切片操作

# 列表切片
my_list = [0,1,2,3,4,5,6]
result1 = my_list[1:4]              #不包含结束坐标本身
print(result1)

# 元组切片
my_tuple = (0,1,2,3,4,5,6)
result2 = my_tuple[:]               # 起始下标、结束下标、步长都可以不写
print(result2)

# 字符串切片
my_str = "0123456"
result3 = my_str[::2]               # 步长为2
print(result3)

# 从头开始到尾结束步长-1
result4 = my_str[::-1]
print(result4)

# 对列表切片，从3开始到1，步长-1
my_list = [0,1,2,3,4,5,6]
result5 = my_list[3:1:-1]
print(result5)


#集合的定义和操作

my_set = {"Andy", "Xu", 666, "Andy", "Xu", 666, "Andy", "Xu", 666}
my_set_empty = set()
print(f"my_set的内容是{my_set}, 类型是{type(my_set)}")
print(f"my_set_empty的内容是{my_set_empty}, 类型是{type(my_set_empty)}")

# 添加新元素
my_set.add("Python")
print(my_set)

# 移除元素
my_set.remove("Andy")
print(my_set)

# 随机取出一个元素
element = my_set.pop()
print(f"取出{element}, 剩下{my_set}")

# 清空集合
my_set.clear()
print(my_set)

# 取2个集合差集
my_set_1 = {1,2,3}
my_set_2 = {1,5,6}
set_difference = my_set_1.difference(my_set_2)
print(set_difference)

# 消除2个集合的差集
my_set_1.difference_update(my_set_2)
print(my_set_1)
print(my_set_2)

# 2个集合合并
my_set_3 = my_set_1.union(my_set_2)
print(my_set_3)

# 统计集合元素数量
print(len(my_set_3))

# 集合的遍历
# 不支持下标索引，故不能用while循环
# 可以用for循环
for element in my_set_3:
    print(element)


# 定义字典
my_dict = {"Andy": 99, "Murat": 100, "Lele": 100, "sb": 62}
# 定义空字
my_dict2 = {}
my_dict3 = dict()
print(f"{my_dict}的类型是{type(my_dict)}")
print(f"{my_dict2}的类型是{type(my_dict2)}")
print(f"{my_dict3}的类型是{type(my_dict3)}")

# 重复key的字典
my_dict4 = {"Andy": 99, "Andy": 100, "Murat": 100, "Lele": 100, "sb": 62}
print(my_dict4)

# 基于key获取value
score = my_dict4["Andy"]
print(score)

# 嵌套字典
stu_score_dict = {
    
    "Andy": {"语文":99, "数学":120, "英语":130},
      "Xu": {"语文":120, "数学":130, "英语":150},
        "Cai": {"语文":90, "数学":110, "英语":100}
}
print(f"学生的考试成绩是:{stu_score_dict}")
print(f"Andy的语文成绩是:{stu_score_dict['Andy']['语文']}")


# 字典新增元素
stu_score_dict["Murat"] = {"语文": 30}
print(f"学生的考试成绩是:{stu_score_dict}")

# 字典更新元素
stu_score_dict['Andy']['语文'] = 130
print(f"学生的考试成绩是:{stu_score_dict}")

# 删除元素
score = stu_score_dict.pop("Xu")
print(score)
print(stu_score_dict)

# 清空元素

stu_score_dict.clear()
print(stu_score_dict)

# 得到字典中的全部key
stu_score_dict = {
    
    "Andy": {"语文":99, "数学":120, "英语":130},
      "Xu": {"语文":120, "数学":130, "英语":150},
        "Cai": {"语文":90, "数学":110, "英语":100}
}

keys = stu_score_dict.keys()
print(keys)

# 遍历字典

# 对key用for循环
for key in keys:
    print(f"字典的key有:{key}")
    print(f"对应的值是:{stu_score_dict[key]}")
# 对字典用for循环
for key in stu_score_dict:
    print(f"字典的key有:{key}")
    print(f"对应的值是:{stu_score_dict[key]}")

# 统计字典内元素数量
len = len(stu_score_dict)
print(len)

# 字符串大小比较
print(f"abd大于abc, 结果是:{('abd' > 'abc')}")
print(f"abd大于ab, 结果是:{('abd' > 'ab')}")
print(f"A大于a, 结果是:{('A' > 'a')}")



# 函数的多返回值

def test_return():
    return 1, "Hello", True

x, y, z = test_return()
print(x)
print(y)
print(z)




# 多种传参形式

def user_info(name, age, gender):
    print(f"姓名是{name}, 年龄是{age}, 性别是{gender}")

# 位置参数
user_info("小明", 20, "男" ) 

# 关键字参数
user_info(name = "小王", age = 20, gender= "女")
user_info(age=20, name="小牛", gender="男")         # 可以不按照顺序
user_info("阿牛", gender="男", age=22)              # 位置参数在前

# 缺省参数
def user_info(name, age, gender = '男'):
    print(f"姓名是{name}, 年龄是{age}, 性别是{gender}")


user_info("大牛", 20)
user_info("大牛", 20, "女")

# 不定长参数

# 位置不定长, *号
def user_info(*args):
    print(f"args参数的类型是:{type(args)}, 内容是:{args}")

user_info(1,2,3,'小明', True)

# 关键字不定长, **号, key-word
def user_info(**kwargs):
    print(f"args参数的类型是:{type(kwargs)}, 内容是:{kwargs}")

user_info(name="小王", age=22, gender="男孩")


# 函数作为参数传递

def test_func(compute):
    result = compute(1,2)
    print(f"compute参数的类型是:{type(compute)}")
    print(f"计算结果:{result}")


def compute(x,y):
    return x + y

# 调用并传入函数
test_func(compute)



# lambda匿名函数
def test_func(compute):
    result = compute(1,2)
    print(f"结果是:{result}")

test_func(lambda x,y: x + y)



# 文件读取

# 打开文件
f = open("C:/Users/admin/Desktop/python/text.txt", "r", encoding="UTF-8")
print(type(f))

# # 读取
# print(f"读取10个字节的结果:{f.read(10)}")
# print(f"读取全部内容为:{f.read()}")

# # 按行读取_readlines
# lines = f.readlines()
# print(f"lines对象的类型:{type(lines)}")
# print(f"按行读取的内容是:{lines}")

# 按行读取_ readline
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()

# print(f"第一行是{line1}")
# print(f"第二行是{line2}")
# print(f"第三行是{line3}")

# readline方法for循环读取
# for line in f:
#     print(f"每一行数据是:{line}")



# 关闭文件  

# 使用time占用文件，期间无法重命名、删除等操作
# time.sleep(500000)

# f.close()


# with open自动关闭文件
with open("C:/Users/admin/Desktop/python/text.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的内容是:{line}")



# 文件写出操作

f = open("C:/Users/admin/Desktop/python/text.txt", "w", encoding="UTF-8")
# write写入
f.write("Hello World!")
# flush刷新
# f.flush()
# close关闭，自带flush功能
f.close()

# 文件追加写入
f = open("C:/Users/admin/Desktop/python/text.txt", "a", encoding="UTF-8")
# write写入
f.write("I'm Andy!")
# flush刷新
# f.flush()
# close关闭，自带flush功能
f.close()



# 异常处理

# 捕获常规异常
try:
    f = open("C:/Users/admin/Desktop/python/abc.txt", "r", encoding="UTF-8")
except:
    print("出现异常了，因为文件不存在，我将用open的方式，使用w模式去打开")
    f = open("C:/Users/admin/Desktop/python/abc.txt", "w", encoding="UTF-8")

# 捕获指定异常
try:
    print(name)

except NameError as e: 
    print("出现了变量未定义的异常")
    print(e)


# 捕获多个异常
try:
    print(name)

except (NameError, ZeroDivisionError) as e:
    print("出现了 变量未定义 或者 零作为分母 的异常")



# 捕获全部异常

try:
    # f = open("C:/Users/admin/Desktop/python/abc.txt", "r", encoding="UTF-8")
    print(name)

except Exception as e:
    print("出现异常了")

else:
    print("没有异常")

# 异常的finally

try:
    f = open("C:/Users/admin/Desktop/python/abc.txt", "r", encoding="UTF-8")
    # print(namme)

except Exception as e:
    print("出现异常了")

else:
    print("没有异常")
finally:
    f.close()


# 异常的传递性
def func1():
    print("func1开始执行")
    num = 1/1
    print("func1结束执行")

def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")

def main():
    func2()

main()


# 导入模块


# import time
# print("你好")
# time.sleep(5)
# print("我好")


# from模块名 import 功能名

# from time import sleep
# print("你好")
# sleep(5)
# print("我好")

# 导入模块全部功能

from time import *
print("你好")
# sleep(5)
print("我好")

# 使用as添加别名
import time as tt
print("你好")
# tt.sleep(5)
print("我好")

# 自定义模块
import my_module1
my_module1.test(1,2)

# 导入包中模块的功能

import my_package.my_module1
import my_package.my_module2

# 演示输出
my_package.my_module1.info_print1()

my_package.my_module2.info_print2()

# 通过__all__变量控制import *
from my_package import *
my_module1.info_print1()
# my_module2.info_print2()          # 这条做不到




# json数据格式转换及数据可视化

import json

# 列表转字符串
data = [{"name": "Andy", "age": "22"}, {"name": "Niu", "age": "23"}, {"name": "徐", "age": "25"}]

json_str = json.dumps(data, ensure_ascii=False)  # ensure_ascii=false之后能正常显示中文
print(json_str)
print(type(json_str))

# 字典转字符串
d = {"name": "Andy", "address": "Hangzhou"}
json_str = json.dumps(d, ensure_ascii=False)  # ensure_ascii=false之后能正常显示中文
print(json_str)
print(type(json_str))


# json字符串转Python数据类型

# 列表
s = '[{"name": "Andy", "age": "22"}, {"name": "Niu", "age": "23"}, {"name": "徐", "age": "25"}]'
l = json.loads(s)
print(l)
print(type(l))

# 字典
s = '{"name": "Andy", "address": "Hangzhou"}'
l = json.loads(s)
print(l)
print(type(l))




# 数据可视化

import pyecharts
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts, ToolboxOpts, VisualMapOpts

line = Line()
line.add_xaxis(["中国", "美国", "英国"])

line.add_yaxis("GDP", [30,20,10])


# 设置全局配置项
line.set_global_opts(
    title_opts = TitleOpts(title="GDP展示", pos_left = "center", pos_bottom = "1%"),            # 水平居中
     legend_opts = LegendOpts(is_show=True),
     toolbox_opts = ToolboxOpts(is_show=True),
     visualmap_opts = VisualMapOpts(is_show=True)
)

line.render()                # 生成图表

# 数据可视化案例
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts



map = Map()
# 准备数据
data = [
    ("北京市", 9),
    ("上海市", 99),
    ("广西壮族自治区", 101),
    ("广东省", 99),
    ("浙江省", 499)
]

map.add("测试地图", data, "china")


# 设置全局选项
map.set_global_opts(
    visualmap_opts = VisualMapOpts(
        is_show = True,
        is_piecewise= True,
        pieces = [
            {"min": 1, "max":9, "label":"1-9", "color": "#CCFFFF" },
            {"min": 10, "max":99, "label":"10-99", "color": "#FF6666" },
            {"min": 100, "max":500, "label":"100-500", "color": "#990033" },
        ]
    )
)


# 绘制地图
map.render()


# 绘制柱状图
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))   
# 反转xy轴
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 20, 10], label_opts=LabelOpts(position="right"))        # 把数字标签的位置移到右边
# 反转xy轴
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [60, 30, 15], label_opts=LabelOpts(position="right"))        # 把数字标签的位置移到右边
# 反转xy轴
bar3.reversal_axis()


# 创建时间线对象并设置主题
timeline = Timeline(
    {"theme": ThemeType.LIGHT}
    )
# 在时间线内添加柱状图对象
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")
# 用时间线对象绘图而不是bar对象
timeline.render("基础时间线柱状图.html")


# 自动播放设置
timeline.add_schema(
    play_interval=100,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True

)

# # 绘制图表
# bar.render("基础柱状图.html")


# 列表的sort方法
my_list = [["a", 33], ["b", 55], ["c", 11]]

# 基于带名函数排序
# def choose_sort_key(element):
#     return element[1]

# my_list.sort(key = choose_sort_key, reverse = True)


# 基于匿名函数排序

my_list.sort(key = lambda element: element[1], reverse=True)

print(my_list)






# 设计一个类(e.g.登记表)
class Student:
    name = None       # 记录血汗俄国姓名
    gender = None     # 记录性别
    nationality = None # 国籍
    native_place = None   # 籍贯
    age = None     # 年龄



# 创建一个对象(e.g.打印登记表)
stu_1 = Student()

# 对象属性赋值(e.g.填写表单)
stu_1.name = "Andy"
stu_1.gender = "male"
stu_1.nationality = "China"
stu_1.native_place = "Hangzhou"
stu_1.age = 23

# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age) 


# 定义一个带有成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f"大家好啊, 我是{self.name}, 请大家多多关照")

    def say_hi2(self, msg):
        print(f"大家好，我是{self.name}, {msg}")                                       #访问成员属性要用self，msg由外部传入不用self

stu = Student()
stu.name = "周杰伦"
stu.say_hi2("哎哟不错哟")

stu2 = Student()
stu2.name = "林俊杰"
stu2.say_hi()



# 类和对象的关系，面向对象编程思路


# 设计一个闹钟类

class Clock:
    id = None
    price = None


    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"闹钟ID:{clock1.id}, 价格:{clock1.price}")

# 内置方法响铃
# clock1.ring()

clock2 = Clock()
clock2.id = "003033"
clock2.price = 21.99
print(f"闹钟ID:{clock2.id}, 价格:{clock2.price}")
# clock1.ring()


# 演示类的构造方法
# 构造方法的名称: __init__()

class Student:
    # name = None
    # age = None
    # tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f"Student类创建了一个类对象")

stu = Student("周杰伦", 66, 13500000666)
print(stu.name)
print(stu.age)
print(stu.tel)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象, name:{self.name}, age:{self.age}"



stu = Student("周杰伦", 66)
print(stu.name)
print(stu.age)
