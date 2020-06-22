"""
    栈
"""


class StackError(Exception):
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


# if __name__ == "__main__":
#     stack = SequenceStack()
#     stack.push(12)
#     stack.push(22)
#     stack.push(33)
#     while not stack.is_empty():
#         print(stack.pop())

data = """Lorem ipsum dolor (sit) amet consectetur adipisicing elit. Corrupti aut (ducimus neque [in mollitia maxime, excepturi impedit, adipisci, veritatis ipsam alias] libero) necessitatibus quidem rem quod tempora? {Tempore, blanditiis vitae}!"""


# for item in data:
#     print(item)

def is_match(left_bracket, right_bracket):
    if left_bracket == "(" and right_bracket == ")":
        return True
    elif left_bracket == "[" and right_bracket == "]":
        return True
    elif left_bracket == "{" and right_bracket == "}":
        return True
    else:
        return False


def detection(data):
    stack = SequenceStack()
    left_brackets = ["(", "[", "{"]
    right_brackets = [")", "]", "}"]
    for item in data:
        if item in left_brackets:
            stack.push(item)
        if item in right_brackets:
            if not is_match(stack.pop(),item):
                return "error"
    if stack.is_empty():
        return "ok"
    return "error"


print(detection(data))
