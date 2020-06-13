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
        @param func_condition: 回调函数（所需要满足的条件）
            参数：列表中的元素
            返回值： 是否满足条件的bool值
        @return: 生成器对象（所查找的元素）
        """
        for item in target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(target, func_condition):
        """
            查找列表中满足条件的第一个元素
        @param target: 列表
        @param func_condition: 回调函数（所需要满足的条件）
            参数：列表中的元素
            返回值： 是否满足条件的bool值
        @return: 元素
        """
        for item in target:
            if func_condition(item):
                return item

    @staticmethod
    def last(target, func_condition):
        """
            查找列表中满足条件的最后一个元素
        @param target: 列表
        @param func_condition: 回调函数（所需要满足的条件）
            参数：列表中的元素
            返回值： 是否满足条件的bool值
        @return: 元素
        """
        for i in range(len(target) - 1, -1, -1):
            if func_condition(target[i]):
                return target[i]

    @staticmethod
    def select(target, func_condition):
        """
            筛选列表中指定成员的数据
        @param target: 列表
        @param func_condition: 回调函数
            参数：列表中的元素
            返回值： 元素中的某个指定成员
        @return: 生成器对象（元素中的成员）
        """
        for item in target:
            yield func_condition(item)

    @staticmethod
    def sum(target, func_condition):
        """
            计算列表中指定条件的所有元素之和
        @param target: 列表
        @param func_condition: 回调函数
            参数：列表中的元素
            返回值： 元素中的某个指定成员
        @return: 指定成员之和（int or float）
        """
        sum_value = 0
        for item in target:
            sum_value += func_condition(item)
        return sum_value

    @staticmethod
    def get_count(target, func_condition):
        """
            获取所有满足条件的对象总数
        @param target: 列表
        @param func_condition: 回调函数（所需要满足的条件）
            参数：列表中的元素
            返回值： 是否满足条件的bool值
        @return: 总数（int）
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
        @param func_condition: 回调函数（所需要满足的条件）
            参数：列表中的元素
            返回值： 是否满足条件的bool值
        @return: bool
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
        @param func_condition: 回调函数（所需要满足的条件）
            参数：列表中的元素
            返回值： 是否满足条件的bool值
        @return: 所删除成员个数（int）
        """
        del_count = 0
        for i in range(len(target) - 1, -1, -1):
            if func_condition(target[i]):
                del target[i]
                del_count += 1
        return del_count

    @staticmethod
    def get_max(target, func_condition):
        """
            获取符合指定条件的最大元素（第一个）
        @param target: 列表
        @param func_condition: 回调函数
            参数：列表中的元素
            返回值： 元素中的某个指定成员
        @return: 元素
        """
        max_value = target[0]
        for i in range(1, len(target)):
            if func_condition(max_value) < func_condition(target[i]):
                max_value = target[i]
        return max_value

    @staticmethod
    def order_by(target, func_condition):
        """
            根据指定条件升序排列
        @param target: 列表
        @param func_condition: 回调函数
            参数：列表中的元素
            返回值： 元素中的某个指定成员
        @return: True
        """
        for i in range(len(target) - 1):
            for j in range(i + 1, len(target)):
                if func_condition(target[i]) > func_condition(target[j]):
                    target[i], target[j] = target[j], target[i]
        return True
