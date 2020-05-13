"""
    封装
"""


# class Student:
#     def __init__(self, name="", age=0):
#         # self.set_name(name)
#         self.name = name  # 调用 @name.setter 修饰的方法
#         # self.set_age(age)
#         self.age = age  # 调用 @age.setter 修饰的方法
#
#     # def get_name(self):
#     #     return self.__name
#
#     @property  # 拦截读取变量的操作
#     def name(self):  # get_name()
#         return self.__name
#
#     @name.setter  # 拦截写入变量的操作
#     def name(self, value):  # set_name()
#         self.__name = value
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if 7 <= value <= 22:
#             self.__age = value
#         else:
#             self.__age = 0
#             print("err")
#
#
# s01 = Student("zf", 2)
# print(s01.name, s01.age)


# class Student:
#     def __init__(self, name=""):
#         self.name = name
#
#     def get_name(self):
#         print("get")
#         return self.__name
#
#     def set_name(self, value):
#         print("set")
#         self.__name = value
#     # 拦截对变量 name 的读写操作
#     # 创建 property 对象， name 存储的是对象地址
#     # 注意：创建对象时，需要传递读写方法
#     name = property(get_name, set_name)


# s01 = Student("zf")
# s01.name = "cf"
# print(s01.name)

# class Student:
#     def __init__(self, name=""):
#         self.__name = name
#
#     # 只读属性
#     # 本质：创建 property 对象， name 存储对象地址
#     # 注意：创建对象时，会指定读取方法
#     # 相当于：name = property(get_name)
#
#     @property
#     def name(self):
#         return self.__name
#
#
# s01 = Student("zf", 2)
# print(s01.name, s01.age)

class Student:
    def __init__(self, name=""):
        self.name = name

    def set_name(self, value):  # set_name()
        self.__name = value

    name = property(None, set_name)


s01 = Student("zfzf")
print(s01._Student__name)
