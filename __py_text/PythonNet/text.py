class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    def init_list(self, data):
        self.head = Node(None)
        p = self.head
        for i in data:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next
        while p:
            print(p.val, end=" ")
            p = p.next
        print()


list_data = [1, 23, 4, 5, 6]
link = LinkList()
link.init_list(list_data)
link.show()
