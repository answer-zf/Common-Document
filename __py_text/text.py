"""

"""


class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, verhical, str_pos):
        verhical.transport(str_pos)


class Verhical:
    def transport(self, str_pos):
        raise NotImplementedError


class Car(Verhical):
    def transport(self, str_pos):
        print("drive", str_pos)


class Airplane(Verhical):
    def transport(self, str_pos):
        print("fly", str_pos)


p01 = Person("zf")
p01.go_to(Car(), "db")
p01.go_to(Airplane(), "db")
