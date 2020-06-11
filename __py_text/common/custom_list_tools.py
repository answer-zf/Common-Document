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
        for i in range(len(target) - 1, -1, -1):
            if func_condition(target[i]):
                return target[i]

    @staticmethod
    def get_count(target, func_condition):
        """
            获取所有满足条件的对象总数
        @param target: 列表
        @param func_condition: 条件
        @return:
        """
        count_value = 0
        for item in target:
            if func_condition(item):
                count_value += 1
        return count_value

    @staticmethod
    def exist(target, func_condition):
        """
            判断是否包含满足条件的对象
        @param target: 列表
        @param func_condition: 条件
        @return: type: bool
        """
        for item in target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def delete_all(target, func_condition):
        """
            删除所有满足条件的对象（成员）
        @param target: 列表
        @param func_condition: 条件
        @return: 删除成员数量
        """
        del_count = 0
        for i in range(len(target) - 1, -1, -1):
            if func_condition(target[i]):
                del target[i]
                del_count += 1
        return del_count
