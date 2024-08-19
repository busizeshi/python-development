import os
import glob
import fnmatch
import datetime
import zipfile


def fun2():
    # 获取路径下的所有文件
    files = os.listdir(r"D:\python\python-development\resource")
    print(files)  # ['images', 'texts']

    is_file = os.path.isfile(files[0])
    is_directory = os.path.isdir(files[0])
    print(is_file)
    print(is_directory)

    files = os.scandir(os.getcwd())
    for file in files:
        print(file.name)


def fun1():
    """
    文件路径操作
    """
    # 获取当前文件的文件夹
    path = os.getcwd()
    print(path)
    # 文件路径拼接
    path = os.path.join(path, 'test.txt')
    print(path)
    is_exist = os.path.exists(path)
    print(is_exist)


def fun3():
    """
    文件遍历与查询
    :return:
    """
    for path, dirs, files in os.walk(r"D:\python\python-development\resource"):
        print(path)
        print(dirs)
        print(files)

    print('-'.ljust(40, '-'))
    print(glob.glob('**/*.txt', recursive=True))


def fun4():
    print(fnmatch.fnmatch('test.txt', '*.txt'))


def fun5():
    # datetime模块下的方法
    print(datetime.datetime.now())
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 获取年月日
    print(datetime.datetime.now().strftime('%Y-%m-%d'))


def fun6():
    """
    创建文件、文件夹与删除
    :return:
    """
    # 创建文件夹
    print(os.mkdir('test'))
    # 删除文件夹
    print(os.rmdir(r'D:\python\python-development\fileoperation\test'))


def fun7():
    """
    文件读写
    :return:
    """
    f = open(r'D:\python\python-development\resource\texts\滕王阁序.txt', 'r', encoding='utf-8')
    text = f.readlines()
    for line in text:
        print(line)
    f.close()

    with open(r'D:\python\python-development\resource\texts\滕王阁序.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
        for line in text:
            print(line)

    with open(r'D:\python\python-development\resource\texts\text1.txt', 'w', encoding='utf-8') as f:
        f.write('hello world')


def fun8():
    """
    压缩与解压缩操作
    :return:
    """
    # 文件压缩
    with zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
        for path, dirs, files in os.walk(r'D:\python\python-development\resource'):
            for file in files:
                zf.write(os.path.join(path, file))
    # 压缩包解压缩
    with zipfile.ZipFile('test.zip', 'r') as zf:
        zf.extractall()


if __name__ == '__main__':
    # fun1()
    # fun2()
    # fun3()
    # fun4()
    # fun5()
    # fun6()
    # fun7()
    fun8()
