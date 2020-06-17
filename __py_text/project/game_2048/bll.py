"""

"""


class GameCoreController:
    def __init__(self):
        self.__map = [
            [2, 0, 4, 2],
            [2, 2, 0, 0],
            [2, 0, 4, 4],
            [4, 0, 0, 2],
        ]
        self.__list_merge = []

    @property
    def map(self):
        return self.__map

    def zero_to_end(self):
        for r in range(len(self.__list_merge) - 1, -1, -1):
            if not self.__list_merge[r]:
                del self.__list_merge[r]
                self.__list_merge.append(0)

    def merge(self):
        self.zero_to_end()
        for r in range(len(self.__list_merge) - 1):
            if self.__list_merge[r] == self.__list_merge[r + 1]:
                self.__list_merge[r] += self.__list_merge[r + 1]
                self.__list_merge[r + 1] = 0
        self.zero_to_end()

    def move_left(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r]
            self.merge()
            self.__map[r][:] = self.__list_merge

    def move_right(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r][::-1]
            self.merge()
            self.__map[r][::-1] = self.__list_merge

    def move_up(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(4):
                self.__list_merge.append(self.__map[r][c])
            self.merge()
            for r in range(4):
                self.__map[r][c] = self.__list_merge[r]

    def move_down(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(3, -1, -1):
                self.__list_merge.append(self.__map[r][c])
            self.merge()
            for r in range(3, -1, -1):
                self.__map[r][c] = self.__list_merge[3 - r]


# test
def print_map(map):
    for r in range(len(map)):
        for column in range(len(map[r])):
            print(map[r][column], end=" ")
        print()

if __name__  == "__main__":


g01 = GameCoreController()
# print_map(g01.map)
# print("------------------")
# g01.move_down()
# print_map(g01.map)
