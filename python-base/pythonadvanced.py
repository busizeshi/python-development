import os

# python高级

"""
文件操作级

# text1 = open(r'D:\python\python-development\resource\texts\text1.txt', 'w')
# text2= open(r'D:\python\python-development\resource\texts\滕王阁序.txt', 'rb')

# 文件写入
# text.write('hello world')

# writelines方法
# text1.writelines(['hello world\n', 'hello world\n', 'hello world\n'])

# 文件读取
# print(text2.readlines())

# 读取图片,并展示
# img = open(r'D:\python\python-development\resource\images\徐大力1.jpg')

# 获取文件地址
# img_path = os.path.abspath(img.name)
# print(img_path)

# 文件重命名
# os.rename(r'D:\python\python-development\resource\images\徐大力1.jpg',
#           r'D:\python\python-development\resource\images\徐大力2.jpg')
# os.remove(r'D:\python\python-development\resource\images\徐大力2.jpg')
os.mkdir(r'D:\python\python-development\resource\tmp')
os.rmdir(r'D:\python\python-development\resource\tmp')
# 获取当前目录
print(os.getcwd())
# 获取当前目录下的所有文件
print(os.listdir())
"""

"""
面向对象

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')

    # 析构方法
    def __del__(self):
        print('Dog ' + self.name.title() + ' is destroyed.')


dog1 = Dog('willie', 6)
dog1.sit()
dog1.roll_over()
del dog1

# 继承
class Cat(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def eat(self):
        print(self.name.title() + ' is eating.')
"""

"""
异常及其处理

try:
    print(5 / 0)
except ZeroDivisionError:
    print('You can not divide by zero!')
else:
    print('No exception was raised.')
finally:
    print('This will always be printed.')
"""
