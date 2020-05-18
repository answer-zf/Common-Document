"""

"""


# class Weapon:
#     def __init__(self, attack):
#         self.attack = attack
#
#     def to_buy(self):
#         print("to buy")
#
#     def atk(self):
#         raise NotImplementedError
#
#
# class Gun(Weapon):
#     def __init__(self, attack, speed):
#         super().__init__(attack)
#         self.speed = speed
#
#     def atk(self):
#         print("gun atk")
#
#
# class Staff_manager:
#     def __init__(self):
#         self.__list_staff = []
#
#     def add(self, value):
#         if isinstance(value, Staff):
#             self.__list_staff.append(value)
#
#     def get_total_salary(self):
#         total_salary = 0
#         for item in self.__list_staff:
#             total_salary += item.get_salary()
#         return total_salary
#
#
# class Staff:
#     def get_salary(self):
#         raise NotImplementedError
#
#
# class Conmmon_staff(Staff):
#     def __init__(self, basic_salary):
#         self.basic_salary = basic_salary
#
#     def get_salary(self):
#         return self.basic_salary
#
#
# class Programer(Staff):
#     def __init__(self, basic_salary, part):
#         self.basic_salary = basic_salary
#         self.part = part
#
#     def get_salary(self):
#         return self.basic_salary + self.part
#
#
# class Seller(Staff):
#     def __init__(self, basic_salary, part):
#         self.basic_salary = basic_salary
#         self.part = part
#
#     def get_salary(self):
#         return self.basic_salary + self.part
#
#
# c01 = Conmmon_staff(100)
# p01 = Programer(120, 12)
# s01 = Seller(110, 11)
# s02 = Staff_manager()
# s02.add(c01)
# s02.add(p01)
# s02.add(s01)
# print(s02.get_total_salary())

class EmployeeManager:
    """
        员工管理器
    """
    def __init__(self):
        self.__employee = []

    def get_total_salary(self):
        """
            获取总薪资
        @return:
        """
        total_salary = 0
        for item in self.__employee:
            total_salary += item.get_salary()
        return total_salary

    def add_employee(self, value):
        """
            添加员工
        @param value:员工对象
        @return:
        """
        if not isinstance(value, Employee):
            return
        self.__employee.append(value)


class Employee:
    """
        普通员工类 即 父类
    """
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    def get_salary(self):
        return self.basic_salary


class Programer(Employee):
    """
        程序员类
    """
    def __init__(self, basic_salary, extra):
        super().__init__(basic_salary)
        self.extra = extra

    def get_salary(self):
        return super().get_salary() + self.extra


class Seller(Employee):
    """
        销售类
    """
    def __init__(self, basic_salary, extra):
        super().__init__(basic_salary)
        self.extra = extra

    def get_salary(self):
        return super().get_salary() + self.extra


e01 = Employee(100)
p01 = Programer(100, 30)
s01 = Seller(100, 10)
e03 = EmployeeManager()
e03.add_employee(e01)
e03.add_employee(p01)
e03.add_employee(s01)
print(e03.get_total_salary())
