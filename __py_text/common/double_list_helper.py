"""
    二维列表工具
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
        """
            按指定方位获取二维数组
        @param list_target: 二维数组
                type: list
        @param v_pos: 二维数组参照位置
                type: function
                ex. Vector2(x, y)
        @param v_dir: 二维数组移动方位
                Vector2 类中定义相应的移动方向的方法
                type: function
                ex. Vector2.direction()
        @param count: 获取的个数
                type: int
        @return:
        """
        get_list = []
        for i in range(count):
            v_pos.x += v_dir.x
            v_pos.y += v_dir.y
            get_list.append(list_target[v_pos.x][v_pos.y])
        return get_list
