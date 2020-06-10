"""
    针对列表的自定义工具
"""


class ListHelper:
    """
        普通（一维）列表自定义工具
    """

    @staticmethod
    def find_all(target, func_condition):
        """
            查找列表中满足条件的所有元素
        @param target: 列表
        @param func_condition: 条件
            函数/方法类型参数
            参数：列表中的元素
            返回值： 是否满足条件的bool值
        @return:
        """
        for item in target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(target, func_condition):
        """
            查找列表中满足条件的第一个元素
        @param target: 列表
        @param func_condition: 条件
        @return:
        """
        for item in target:
            if func_condition(item):
                return item

    @staticmethod
    def select(target, func_condition):
        """
            筛选列表中指定成员的数据
        @param target: 列表
        @param func_condition: 条件
        @return:
        """
        for item in target:
            yield func_condition(item)

    @staticmethod
    def sum(target, func_condition):
        """
            计算列表中指定条件的所有元素之和
        @param target: 列表
        @param func_condition: 条件
        @return:
        """
        sum_value = 0
        for item in target:
            sum_value += func_condition(item)
        return sum_value

    @staticmethod
    def last(target, func_condition):
        """
            查找列表中满足条件的最后一个元素
        @param target: 列表
        @param func_condition: 条件
        @return:
        """
        # result = [item for item in target if item.hp != 0 ]
        # return result[-1]
        for item in target[::-1]:
            if func_condition(item):
                return item


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
