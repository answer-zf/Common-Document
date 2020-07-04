class Sort:
    def __init__(self, list_target):
        self.list_target = list_target

    def bubble(self):
        """
            冒泡排序
        @return:
        """
        for i in range(len(self.list_target) - 1):  # 比较多少轮
            for j in range(len(self.list_target) - i - 1):  # 每轮比较多少次
                if self.list_target[j] > self.list_target[j + 1]:
                    self.list_target[j], self.list_target[j + 1] = self.list_target[j + 1], self.list_target[j]

    def selection(self):
        """
            选择排序
        @return:
        """
        for i in range(len(self.list_target) - 1):
            target_min = i
            for j in range(i + 1, len(self.list_target)):
                if self.list_target[i] > self.list_target[j]:
                    # self.list_target[i], self.list_target[j] = self.list_target[j], self.list_target[i]
                    target_min = j
            if target_min != i:
                self.list_target[i], self.list_target[target_min] = self.list_target[target_min], self.list_target[i]

    def insertion(self):
        """
            插入排序
        @return:
        """
        for i in range(1, len(self.list_target)):
            mark = self.list_target[i]
            j = i
            while j > 0 and self.list_target[j - 1] > mark:
                self.list_target[j] = self.list_target[j - 1]
                j -= 1
                self.list_target[j] = mark

    def quick(self, low, high):
        """
            快速排序
                low 列表开头元素索引
                high 列表结尾元素索引
        @return:
        """
        if low < high:
            key = self.sub_quick(low, high)
            self.quick(0, key - 1)
            self.quick(key + 1, high)

    def sub_quick(self, low, high):
        """
            单次快速排序
        @param low:
        @param high:
        @return:
        """
        key = self.list_target[low]
        while low < high:
            while low < high and self.list_target[high] >= key:
                high -= 1
            self.list_target[low] = self.list_target[high]
            while low < high and self.list_target[low] < key:
                low += 1
            self.list_target[high] = self.list_target[low]
        self.list_target[low] = key
        return low


if __name__ == "__main__":
    list01 = [1, 2, 3, 4, 9, 0, 7, 5, 6, 4, 2]
    # Sort(list01).bubble()
    # Sort(list01).selection()
    Sort(list01).quick(0, len(list01) - 1)
    print(list01)
