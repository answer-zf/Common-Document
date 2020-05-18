"""
    student-manager
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

    def update_student(self, id, name, age, score):
        """
            更新学生
        @param id: 要更新的学生 id
        @return:
        """
        for item in self.__list_stu:
            if item.id == id:
                item.name = name
                item.age = age
                item.score = score
            return True
        else:
            return False


class StudentManagerView:
    """
        界面视图类
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def __input_students(self):
        """
            输入学生
        :return:
        """
        stu = StudentModel()
        stu.name = input("student name : ")
        stu.age = int(input("student age : "))
        stu.score = int(input("student score : "))
        self.__manager.add_student(stu)

    def __output_students(self, list_target):
        """
            显示学生列表信息
        @param list_target:
        @return:
        """
        for item in list_target:
            print("id:%d, name:%s, age:%d, score:%d" %
                  (item.id, item.name, item.age, item.score))

    def __output_students_by_score(self):
        """
            按成绩升序排列学生列表
        @return: 按成绩升序排列的新学生列表
        """
        list_target = self.__manager.order_by_score()
        self.__output_students(list_target)

    def __delete_student(self):
        id = int(input("pl. input id for del stu"))
        if self.__manager.remove_student(id):
            print("del complete")
        else:
            print("del error")

    def __update_student(self):
        id = int(input("pl. input id for update stu"))
        name = input("name:")
        age = int(input("age:"))
        score = int(input("score:"))
        if self.__manager.update_student(id, name, age, score):
            print("update complete")
        else:
            print("update error")

    def __display_menu(self):
        """
            显示菜单
        :return:
        """
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩降序排列")

    def __select_menu(self):
        """
            选择菜单
        :return:
        """
        str_number = input("pl. input option")
        if str_number == "1":
            self.__input_students()
        elif str_number == "2":
            self.__output_students(self.__manager.list_stu)
        elif str_number == "3":
            self.__delete_student()
        elif str_number == "4":
            self.__update_student()
        elif str_number == "5":
            self.__output_students_by_score()

    def main(self):
        """
            界面入口方法
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()


view = StudentManagerView()
view.main()
