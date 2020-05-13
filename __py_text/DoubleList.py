"""

"""


class Vector2:
    """
        向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def right_up():
        return Vector2(-1, 1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def down():
        return Vector2(1, 0)

    @staticmethod
    def left():
        return Vector2(0, -1)


class DoubleListHelper:
    """
        二维列表助手:
            在开发过程中，所有对二维列表的常用操作
    """

    @staticmethod
    def get_elements(list_target, v_pos, v_dir, count):
        get_list = []
        for i in range(count):
            v_pos.x += v_dir.x
            v_pos.y += v_dir.y
            get_list.append(list_target[v_pos.x][v_pos.y])
        return get_list


# 测试
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
    ["30", "31", "32", "33"],
]
#
# re = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
# print(re)
re = DoubleListHelper.get_elements(list01, Vector2(2, 3), Vector2.left(), 3)
print(re)
re = DoubleListHelper.get_elements(list01, Vector2(0, 2), Vector2.down(), 2)
print(re)
re = DoubleListHelper.get_elements(list01, Vector2(2, 0), Vector2.right_up(), 2)
print(re)
