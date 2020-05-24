"""
    bll 业务逻辑层
"""


class StudentManagerController:
    """
        学生逻辑控制器
    """

    def __init__(self):
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu

    def add_student(self, student):
        """
            添加新学生
        :param student: 需要添加的学生对象
        :return:
        """
        student.id = self.__generate_id()
        self.__list_stu.append(student)

    def __generate_id(self):
        """
            生成编号
        :return: 编号
        """
        # if len(self.__list_stu) > 0:
        #     id = self.__list_stu[-1].id + 1
        # else:
        #     id = 1
        return self.__list_stu[-1].id + 1 if len(self.__list_stu) > 0 else 1

    def order_by_score(self):
        """
            按成绩升序排列
        @return: 升序排列新学生列表
        """
        new_list = self.__list_stu[:]
        for i in range(len(new_list) - 1):
            for j in range(i + 1, len(new_list)):
                if new_list[i].score >= new_list[j].score:
                    new_list[i], new_list[j] = new_list[j], new_list[i]
        return new_list

    def remove_student(self, id):
        """
            删除学生
        @param id: 要删除的学生 id
        @return:
        """
        # for i in range(len(self.__list_stu)):
        #     if self.__list_stu[i].id == id:
        #         # del self.__list_stu[i]
        #         # print("del complete")
        #         # break
        #         self.__list_stu.remove(self.__list_stu[i])
        # else:
        #     print("id: error")
        for item in self.__list_stu:
            if item.id == id:
                self.__list_stu.remove(item)
                return True
        return False

    def update_student(self, stu):
        """
            更新学生
        @param id: 要更新的学生 id
        @return:
        """
        for item in self.__list_stu:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        return False
