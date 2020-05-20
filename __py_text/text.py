"""

"""


class StudentModel:
    """
        学生数据模型类
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
            创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return "id is %d, name is %s, age is %d, score is %d" % (self.id, self.name, self.age, self.score)

    def __repr__(self):
        return 'StudentModel("%s", %d, %d)' % (self.name, self.age, self.score)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value


s01 = StudentModel('zf', 12, 90)
print(s01)
re = eval(s01.__repr__())
print(re)
list_01 = ["zf", 44, 99]