"""
    ui界面（表示层）
"""
from StudentManager.model import *
from StudentManager.bll import *


class StudentManagerView:
    """
        界面视图类
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def __get_student_item(self,student_item,start_num,end_num):
        try:
            int_student_item = int(input("student %s : "%student_item))
        except ValueError:
            print("err: input int")
        if start_num <= int_student_item <= end_num:
            return int_student_item
        else:
            print("error")

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

    def __modify_student(self):
        """
            修改学生信息
        @return:
        """
        stu = StudentModel()
        stu.id = int(input("pl. input id for update stu"))
        stu.name = input("name:")
        stu.age = int(input("age:"))
        stu.score = int(input("score:"))
        if self.__manager.update_student(stu):
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
            self.__modify_student()
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
