"""

"""

from multiprocessing import Process
from time import sleep
import os


def th1():
    sleep(3)
    print("th1")
    print(os.getppid(), "------------", os.getpid())


def th2():
    sleep(2)
    print("th2")
    print(os.getppid(), "------------", os.getpid())


def th3():
    sleep(4)
    print("th3")
    print(os.getppid(), "------------", os.getpid())


things = [th1, th2, th3]
jobs = []
for th in things:
    p = Process(target=th)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
