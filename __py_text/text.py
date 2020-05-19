"""

"""


class Employee:
    """
        普通员工类 即 父类
    """

    def __init__(self, name, job):
        self.name = name
        self.job = job  # 依赖

    def calcular_salary(self):
        return self.job.get_salary()


class Job:
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    def get_salary(self):
        return self.basic_salary


class Programer(Job):  # 关联
    """
        程序员类
    """

    def __init__(self, basic_salary, extra):
        super().__init__(basic_salary)
        self.extra = extra

    def get_salary(self):
        return super().get_salary() + self.extra


class salesmen(Job):
    """
        销售类
    """

    def __init__(self, basic_salary, extra):
        super().__init__(basic_salary)
        self.extra = extra

    def get_salary(self):
        return super().get_salary() + self.extra


lw = Employee("lw", Programer(100, 10))
print(lw.calcular_salary())
lw.job = salesmen(100, 1)
print(lw.calcular_salary())
