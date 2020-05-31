"""

"""

list01 = [1, 23, 4, 56, 6, 7]

# for item in list01:
#     print(item)

# for 循环原理
# 1.  获取迭代器对象
iterator = list01.__iter__()

while True:
    try:  # 如果获取所有元素，则执行 except
        # 2.  获取下一个元素（迭代过程：调用迭代器的__next__方法）
        item = iterator.__next__()
        # 3.  停止迭代：捕获 StopIteration 异常
    except StopIteration:
        break  # 跳出循环
