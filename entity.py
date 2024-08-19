# 用户类
class User:
    def __init__(self, id, code, age, name, height, address):
        self.id = id
        self.code = code
        self.age = age
        self.name = name
        self.height = height
        self.address = address

    # 重构方法
    def __str__(self):
        return "id:{},code:{},age:{},name:{},height:{},address:{}".format(self.id, self.code, self.age, self.name,
                                                                          self.height, self.address)
