"""
    
"""

list01 = [123, 2342, 54, 6546, 9, 46546, 23476, 7]


def get_even(list_target):
    for item in list_target:
        if item % 2 == 0:
            yield item


for item in get_even(list01):
    print(item)
