"""

"""

from double_list_helper import *

# 测试
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
    ["30", "31", "32", "33"],
]
#
# re = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
# print(re)
re = DoubleListHelper.get_elements(list01, Vector2(2, 3), Vector2.left(), 3)
print(re)
re = DoubleListHelper.get_elements(list01, Vector2(0, 2), Vector2.down(), 2)
print(re)
re = DoubleListHelper.get_elements(list01, Vector2(2, 0), Vector2.right_up(), 2)
print(re)