# python基础语法

"""
# 变量
# 整形
a = 1
print(type(a))  # <class 'int'>
# 浮点型
b = 1.1
print(type(b))  # <class 'float'>
# 布尔型
c = True
print(type(c))  # <class 'bool'>
# 字符串
d = 'hello'
print(type(d))  # <class 'str'>
# 列表
e = [1, 2, 3]
print(type(e))  # <class 'list'>
# 元组
f = (1, 2, 3)
print(type(f))  # <class 'tuple'>
# 字典
g = {'a': 1, 'b': 2}
print(type(g))  # <class 'dict'>
# 集合
h = {1, 2, 3}
print(type(h))  # <class 'set'>
"""

"""
格式化输出

age = 18
name = 'hangman'
weight = 80.50
student_id = 1

print('我的名字是%s' % name)
print('我的年龄是%4d' % student_id)
print('我的体重是%5.2f' % weight)
print('我的名字是%s,今年%d' % (name, age))
print('我的名字是{},今年{}'.format(name, age))
print(f'我的名字是{name},明年{age+1}')
"""

"""
格式化输入

name = input('请输入你的名字：')
age = input('请输入你的年龄：')
print(f'我的名字是{name},今年{age}')
"""

"""
数据类型转换

num = 1
num_str = str(num)
print(type(num_str))
float_num = float(num)
print(type(float_num))

t = (1, 2, 3)
t_list = list(t)
print(t_list)  # [1, 2, 3]

str1 = '10'
str2 = '[1,2,3]'
str3 = '{"a":1,"b":2}'
print(type(eval(str1)))  # <class 'int'>
print(type(eval(str2)))  # <class 'list'>
print(type(eval(str3)))  # <class 'dict'>
"""

"""
逻辑运算符转换

a = 1
b = 2

print(a <= 1 and b >= 2)  # True
print(a <= 1 or b >= 2)  # True
print(not a <= 1)  # False
"""

"""
条件语句

a = 1
if a == 1:
    print('a == 1')
elif a == 2:
    print('a == 2')
else:
    print('a != 1 and a != 2')
"""

"""
循环语句

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()

cur = 0
while cur < 10:
    print(cur)
    cur += 1

while cur < 20:
    if cur == 15:
        print('cur == 15')
        break
    cur += 1
    print(cur)

while cur < 20:
    cur += 1
    if cur == 20:
        print('cur == 20')
        continue
    print(cur)

while cur < 25:
    cur += 1
    print(cur)
else:
    print('循环结束')
"""

"""
字符串

s = ' hello,world '
# 字符串索引
print(s[1])  # h
print(s[-2])  # d
print(s[1:4])  # hel
print(s[:4])  # hel
print(s[1:])  # hello,world

# find方法
print(s.find('lo'))
print(s.find('o', 6, 10))

# index方法
print(s.index('o'))
print(s.index('o', 6, 10))

# count方法
print(s.count('o'))
print(s.count('o', 6, 10))

# replace方法
print(s.replace('o', 'O'))
print(s.replace('o', 'O', 1))

# split方法
print(s.split(','))
print(s.split('o', 1))

# join方法
print('-'.join(s))
str_list = ['hello', 'world']
print(','.join(str_list))

# lower方法
print(s.lower())
# upper方法
print(s.upper())
# strip方法
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# ljust方法
print(''.ljust(40, '-'))

# startwith方法
print(s.startswith(' '))

# isdigit方法
print('123'.isdigit())
"""

"""
列表

dogs = ['阿拉斯加', '哈士奇', '萨摩耶', '秋田犬']

# 索引
print(dogs[0])

# len
print(len(dogs))

print('哈士奇' in dogs)

dogs.append('金毛')
print(dogs)

# insert方法
dogs.insert(1, '柯基')
print(dogs)

# pop方法
dogs.pop()
print(dogs)

# remove方法
dogs.remove('秋田犬')
print(dogs)

# sort方法
dogs.sort()
print(dogs)

# reverse方法
dogs.reverse()
print(dogs)

# 列表推导式
nums = [1, 2, 3, 4, 5]
nums_list = [num * 2 for num in nums]
print(nums_list)

# 列表解析
nums_list = [num * 2 for num in nums if num % 2 == 0]
print(nums_list)

# 列表复制
copy_list = dogs.copy()
print(copy_list)

# 列表解包
a, b, c, d= dogs
print(a, b, c, d)

# 列表解包
a, *b, c = dogs
print(a, b, c)

# 列表解包
a, *b = dogs
print(a, b)
"""

"""
元组:不可修改的数据

tuple_list = ('a', 'b', 'c')
print(tuple_list)
print(tuple_list[0])
print(tuple_list[1:])
print(tuple_list.count('a'))
print(tuple_list.index('b'))

dogs = ('阿拉斯加', '哈士奇', '萨摩耶', '秋田犬')
tuple_dogs = list(dogs)
print(tuple_dogs)
"""

"""
字典操作

dogs = {
    'name': '哈士奇',
    'age': 2,
    'color': 'white'
}
print(dogs)
print(dogs['name'])
print(dogs.get('name'))

# 获取键
print(dogs.keys())

# 获取值
print(dogs.values())

# 获取键值对
print(dogs.items())

# 添加键值对
dogs['breed'] = '秋田犬'
print(dogs)

# 修改键值对
dogs['age'] = 3
print(dogs)

# 删除键值对
del dogs['color']
print(dogs)

# 清空字典
dogs.clear()
print(dogs)
"""

"""
函数

def add(a, b):
    res = a + b
    return res


print(add(1, 2))


# 缺省参数
def fun1(a, b=2):
    print(a, b)


fun1(1)
"""
