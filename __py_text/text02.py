"""
    
"""


class Enemy:
    def __init__(self, id, name, attack, hp, speed):
        self.id = id
        self.name = name
        self.attack = attack
        self.hp = hp
        self.speed = speed


list_enemies = [
    Enemy(101, "xlsbz", 60, 10, 9),
    Enemy(102, "jyzj", 100, 0, 6),
    Enemy(103, "lmsj", 40, 9, 5),
    Enemy(104, "rlsz", 80, 0, 2),
    Enemy(105, "slbw", 70, 0, 7),
]

from common.custom_list_tools import ListHelper

# for item in ListHelper.find_all(list_enemies, lambda item: item.hp == 0 ):
#     print(item.name)
#
# enemy_by_id = ListHelper.first(list_enemies, lambda item: item.id == 101)
# print(enemy_by_id.name)
#
# for item in ListHelper.find_all(list_enemies, lambda item: item.hp != 0 ):
#     print(item.name)
#
# sum_attack = ListHelper.sum(list_enemies, lambda item: item.attack)
# print(sum_attack)
#
# for item in ListHelper.find_all(list_enemies, lambda item: 5 < item.speed <= 10 ):
#     print(item.name)
#
# for item in ListHelper.select(list_enemies, lambda item: item.name):
#     print(item)

# last_enemy_hp = ListHelper.last(list_enemies, lambda item: item.hp != 0)
# print(last_enemy_hp.name)
#
# last_enemy_attack = ListHelper.last(list_enemies, lambda item: item.attack > 5 )
# print(last_enemy_attack.name)

class Demo:
    def __init__(self):
        pass

print(type(Demo))