"""

"""


class Player:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def attack(self, enemy):
        print("p d e")
        enemy.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("dead")


class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def attack(self, player):
        player.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        print("e, damage")
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("...")


p01 = Player(100, 20)
e01 = Enemy(30, 10)
p01.attack(e01)
