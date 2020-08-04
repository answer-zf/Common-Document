"""
    ui界面
"""
from bll import GameCoreController
from bll import Direction
import os

class GameConsoleView:
    """
        控制台视图
    """

    def __init__(self):
        self.__game_controller = GameCoreController()

    def start(self):
        self.__game_controller.generate_new_num()
        self.__game_controller.generate_new_num()
        self.__print_interface()

    def update(self):
        """
            更新
        @return:
        """
        while True:
            self.__move_map()
            if self.__game_controller.is_change:
                self.__game_controller.generate_new_num()
                self.__print_interface()
                if self.__game_controller.is_game_over():
                    print("Game Over")
                    break

    def __move_map(self):
        str_dire = input("up: w, down: s, left: a, right: d")
        if str_dire == "w":
            self.__game_controller.move(Direction.up)
        elif str_dire == "s":
            self.__game_controller.move(Direction.down)
        elif str_dire == "a":
            self.__game_controller.move(Direction.left)
        elif str_dire == "d":
            self.__game_controller.move(Direction.right)

    def __print_interface(self):
        """
            打印界面
        @return:
        """
        # 清空控制台
        os.system("clear")
        for r in range(len(self.__game_controller.map)):
            for column in range(len(self.__game_controller.map[r])):
                print(self.__game_controller.map[r][column], end="\t ")
            print()
