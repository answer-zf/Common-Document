"""
    单链表
"""


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkList(object):

    def __init__(self):
        self.head = Node(None)

    def init_link(self, data):
        """
            初始化链式表
        @param data:
        @return:
        """
        p = self.head  # 可移动变量
        for i in data:
            p.next = Node(i)
            p = p.next

    def show(self):
        """
            控制台输出链表
        @return:
        """
        p = self.head.next
        while p:
            print(p.val, end=" ")
            p = p.next
        print()

    def append(self, val):
        """
            尾部插入新结点
        @param val:
        @return:
        """
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(val)

    def get_length(self):
        """
            获取链表长度
        @return:
        """
        n = 0
        p = self.head
        while p.next:
            n += 1
            p = p.next
        return n

    def is_empty(self):
        """
            链表是否为空
        @return:
        """
        if self.get_length():
            return False
        return True

    def clear(self):
        """
            清空链表
        @return:
        """
        self.head.next = None

    def get_item(self, index):
        """
            获取索引值
        @param index:
        @return:
        """
        p = self.head.next
        n = 0

        while p:
            if index >= self.get_length() or index < 0:
                raise IndexError("list index out of range")
            elif index == n:
                return p
            p = p.next
            n += 1
        # while n < index and p:
        #     n += 1
        #     p = p.next
        # if not p:
        #     raise IndexError("list index out of range")
        # return p

    def insert(self, index, val):
        """
            根据索引位置插入数据
        @param index:
        @param val:
        @return:
        """
        node_val = Node(val)
        if index == 0:
            node_val.next = self.get_item(0)
            self.head.next = node_val
        else:
            node_val.next = self.get_item(index - 1).next
            self.get_item(index - 1).next = node_val


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    link = LinkList()
    link.init_link(data)
    # link.append(7)
    # print(link.get_length())
    # print(link.is_empty())
    link.insert(4, 999)
    # print(link.get_item(3).val)
    link.show()
