"""

"""


class Skill:
    pass

# class SkillIterator:
#     def __init__(self, target):
#         self.target = target
#         self.index = 0

#     def __next__(self):
#         # 索引越界抛出异常
#         if self.index >= len(self.target):
#             raise StopIteration()

#         # 返回下一个元素
#         item = self.target[self.index]
#         self.index += 1
#         return item


class SkillManager:
    def __init__(self, skills):
        self.skills = skills

    # def __iter__(self):
    #     return SkillIterator(self.skills)
    def __iter__(self):
        """
            1. 调用 iter 方法未执行
            2. 调用 next 方法时，执行到 yield 语句暂时离开
            3. 再次调用 next 方法时，从上次离开的代码开始执行，到 yield 语句暂时离开
            4. 待执行完方法体，抛出 StopIteration 异常
            原理：如果方法体中包含 yield 关键字，会自动生成迭代器对象
            生成迭代器代码的大致规则：
            1. 将 yield 关键字以前的代码放到 next 方法中
            2. 将 yield 关键字以后的数据作为 next 方法的返回值
        """
        yield self.skills[0]
        yield self.skills[1]
        yield self.skills[2]


manager = SkillManager([Skill(), Skill(), Skill()])

# for item in manager:  # 获取 manager 对象中集合（聚合）类型对象元素
#     print(item)

iterator = manager.__iter__()

while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration as e:
        print(e)
        break
