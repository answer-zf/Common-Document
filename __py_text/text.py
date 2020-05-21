"""

"""


class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector(self.x + other)

    def __iadd__(self, other):
        self.x += other
        return self

    def __str__(self):
        return "x: %s" % self.x


v01 = Vector(10)
v01 += 5
print(v01)

