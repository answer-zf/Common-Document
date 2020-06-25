"""
    队列
"""

from link_list import Node


class QueueError(Exception):
    """
        队列异常
    """
    pass


class SequenceQueue:
    """
        队列的顺序存储结构
    """

    def __init__(self):
        self._element = []

    def is_empty(self):
        return self._element == []

    def append(self, val):
        self._element.append(val)

    def pop(self):
        if not self._element:
            raise QueueError("Queue is empty")
        return self._element.pop(0)


class LinkQueue:
    """
        队列的链式存储结构
            左侧对头，右侧队尾
    """

    def __init__(self):
        # Node(None) 可以是任意结点（无任何作用），一整条队列
        # front 的作用 类似一个指针，指向队尾的前一个结点
        self._front = self._rear = Node(None)

    def is_empty(self):
        """
            非空验证
        @return:
        """
        return self._front is self._rear

    def append(self, val):
        """
            入队
        @param val:
        @return:
        """
        self._rear.next = Node(val)
        self._rear = self._rear.next

    def pop(self):
        """
            出队
        @return:
        """
        if self._front is self._rear:
            raise QueueError("Queue is empty")
        self._front = self._front.next
        return self._front.val

    def clear(self):
        self._front = self._rear

if __name__ == "__main__":
    queue = LinkQueue()
    queue.append(10)
    queue.append(20)
    queue.append(30)
    while not queue.is_empty():
        print(queue.pop())