"""
    游戏逻辑
"""
from model import Location
import random
import copy


class GameCoreController:
    """
        游戏核心控制器
    """

    def __init__(self):
        self.__map = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4,
        ]
        # 存储去零合并的列表
        self.__list_merge = []
        # 空位置的列表
        self.__list_empty_location = []
        self.is_change = False

    @property
    def map(self):
        return self.__map

    @property
    def is_change(self):
        return self.__is_change

    @is_change.setter
    def is_change(self, value):
        self.__is_change = value

    def __zero_to_end(self):
        for r in range(len(self.__list_merge) - 1, -1, -1):
            if not self.__list_merge[r]:
                del self.__list_merge[r]
                self.__list_merge.append(0)

    def __merge(self):
        self.__zero_to_end()
        for r in range(len(self.__list_merge) - 1):
            if self.__list_merge[r] == self.__list_merge[r + 1]:
                self.__list_merge[r] += self.__list_merge[r + 1]
                self.__list_merge[r + 1] = 0
        self.__zero_to_end()

    def __move_left(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r]
            self.__merge()
            self.__map[r][:] = self.__list_merge

    def __move_right(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r][::-1]
            self.__merge()
            self.__map[r][::-1] = self.__list_merge

    def __move_up(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(4):
                self.__list_merge.append(self.__map[r][c])
            self.__merge()
            for r in range(4):
                self.__map[r][c] = self.__list_merge[r]

    def __move_down(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(3, -1, -1):
                self.__list_merge.append(self.__map[r][c])
            self.__merge()
            for r in range(3, -1, -1):
                self.__map[r][c] = self.__list_merge[3 - r]

    def move(self, dir):
        """
            移动
        @param dir: Direction 类型
        @return:
        """
        self.__is_change = False
        origin_map = copy.deepcopy(self.__map)
        if dir == Direction.up:
            self.__move_up()
        elif dir == Direction.down:
            self.__move_down()
        elif dir == Direction.left:
            self.__move_left()
        elif dir == Direction.right:
            self.__move_right()
        self.__is_change = self.__equal_map(origin_map)

    def __equal_map(self, origin):
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if origin[r][c] != self.__map[r][c]:
                    return True
        return False

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(Location(r, c))

    def generate_new_num(self):
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2
        self.__list_empty_location.remove(loc)

    def is_game_over(self):
        if len(self.__list_empty_location) == 0 and not self.is_change:
            return True
        return False



class Direction:
    """
        方向
    """
    up = 0
    down = 1
    left = 2
    right = 3
