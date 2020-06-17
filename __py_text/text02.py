"""

"""
import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        old_time = time.time()
        result = func(*args, **kwargs)
        time.time() - old_time
        print(time.time() - old_time)
        return result

    return wrapper


class Student:
    def __init__(self, name):
        self.name = name

    @print_execute_time
    def study(self):
        print("study")
        time.sleep(2)


s01 = Student("zf")
s01.study()
