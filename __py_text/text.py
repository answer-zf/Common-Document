"""

"""


class Weapon:
    def __init__(self, atk):
        self.atk = atk

    def attack(self, *args):
        for item in args:
            item.damaged(self.atk)


class Damageable:
    def __init__(self, hp):
        self.hp = hp

    def damaged(self, value):
        raise NotImplementedError


class Player(Damageable):

    def damaged(self, value):
        self.hp -= value
        print("player damage")


class Enemy(Damageable):

    def damaged(self, value):
        self.hp -= value
        print("enemy damage")


w01 = Weapon(10)
p01 = Player(100)
e01 = Enemy(100)
w01.attack(p01, e01)
