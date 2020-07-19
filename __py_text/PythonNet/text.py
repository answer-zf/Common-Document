"""

"""

from multiprocessing import Semaphore, Process
from time import sleep
import os

sem = Semaphore(3)


def fun():
    print("%d ready" % os.getpid())
    sem.acquire()
    print("%d start" % os.getpid())
    sleep(3)
    print("%d end" % os.getpid())
    sem.release()


jobs = []

for i in range(5):
    p = Process(target=fun)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
