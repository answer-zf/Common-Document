"""
    2048 core algorithm
"""


def zero_to_end(list_target):
    # new_list = [item for item in list_target if item != 0]
    # new_list += [0] * list_target.count(0)
    # list_target[:] = new_list[:]
    for i in range(len(list_target) - 1, -1, -1):
        if not list_target[i]:
            del list_target[i]
            list_target.append(0)


def merge(list_target):
    zero_to_end(list_target)

    for i in range(len(list_target) - 1):
        if list_target[i] == list_target[i + 1]:
            list_target[i] += list_target[i + 1]
            list_target[i + 1] = 0

    zero_to_end(list_target)


def print_map(map):
    for row in range(len(map)):
        for column in range(len(map[row])):
            print(map[row][column], end=" ")
        print()


def move_left(map):
    for row in range(len(map)):
        merge(map[row])


def move_right(map):
    for row in range(len(map)):
        list_merge = map[row][::-1]
        # print(list_merge)
        merge(list_merge)
        map[row][::-1] = list_merge


def move_up(map):
    for c in range(4):
        list_merge = []
        for r in range(4):
            list_merge.append(map[r][c])

        merge(list_merge)

        for r in range(4):
            map[r][c] = list_merge[r]


def move_down(map):
    for c in range(4):
        list_merge = []
        for r in range(3, -1, -1):
            list_merge.append(map[r][c])

        merge(list_merge)

        for r in range(3, -1, -1):
            map[r][c] = list_merge[3 - r]


list01 = [2, 2, 4, 0]
list02 = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2]
]
# merge(list01)
print_map(list02)
print("-------")
move_down(list02)
print_map(list02)
