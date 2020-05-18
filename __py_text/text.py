"""

"""


class Weapon:
    def __init__(self, attack):
        self.attack = attack

    def to_buy(self):
        print("to buy")

    def atk(self):
        raise NotImplementedError


class Gun(Weapon):
    def __init__(self, attack, speed):
        super().__init__(attack)
        self.speed = speed

    def atk(self):
        print("gun atk")


class Staff_manager:
    def __init__(self):
        self.__list_staff = []

    def add(self, value):
        if isinstance(value, Staff):
            self.__list_staff.append(value)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__list_staff:
            total_salary += item.get_salary()
        return total_salary


class Staff:
    def get_salary(self):
        raise NotImplementedError


class Conmmon_staff(Staff):
    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    def get_salary(self):
        return self.basic_salary


class Programer(Staff):
    def __init__(self, basic_salary, part):
        self.basic_salary = basic_salary
        self.part = part

    def get_salary(self):
        return self.basic_salary + self.part


class Seller(Staff):
    def __init__(self, basic_salary, part):
        self.basic_salary = basic_salary
        self.part = part

    def get_salary(self):
        return self.basic_salary + self.part


c01 = Conmmon_staff(100)
p01 = Programer(120, 12)
s01 = Seller(110, 11)
s02 = Staff_manager()
s02.add(c01)
s02.add(p01)
s02.add(s01)
print(s02.get_total_salary())
