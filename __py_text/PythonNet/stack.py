"""
    栈
"""

from link_list import Node


class StackError(Exception):
    """
        栈的异常
    """
    pass


class SequenceStack(object):
    """
        栈的顺序存储结构
    """

    def __init__(self):
        self._elements = []

    def top(self):
        if not self._elements:
            raise StackError("Stack is empty")
        return self._elements[-1]

    def is_empty(self):
        return self._elements == []

    def push(self, val):
        """
            入栈
        @param val:
        @return:
        """
        self._elements.append(val)

    def pop(self):
        """
            出栈
        @return:
        """
        if not self._elements:
            raise StackError("Stack is empty")
        return self._elements.pop()


class LinkStack(object):
    """
        栈的链式存储结构
    """

    def __init__(self):
        # 标记栈顶位置
        self._top = None

    def is_empty(self):
        """
            非空验证
        @return:
        """
        return not self._top

    def push(self, val):
        """
            入栈
        @param val:
        @return:
        """
        self._top = Node(val, self._top)
        # node_val = Node(val)
        # node_val.next = self._top
        # self._top = node_val

    def pop(self):
        """
            弹栈
        @return:
        """
        if not self._top:
            raise StackError("stack is empty")
        p = self._top
        self._top = p.next
        return p.val

    def get_top(self):
        """
            获取栈顶元素值
        @return:
        """
        if self.is_empty():
            raise StackError("stack is empty")
        return self._top.val

    def clear(self):
        """
            清栈
        @return:
        """
        self._top = None


if __name__ == "__main__":
    stack = LinkStack()
    print(stack.is_empty())
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.get_top(),"-----")
    while not stack.is_empty():
        print(stack.pop())
