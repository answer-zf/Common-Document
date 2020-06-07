"""
    针对列表的自定义工具
"""

class ListHelper:

    @staticmethod
    def find_all(target,func_condition):
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

