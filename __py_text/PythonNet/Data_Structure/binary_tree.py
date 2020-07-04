"""
    二叉树的构建与遍历
"""

from queue import SequenceQueue


class TreeNode:
    """
        二叉树节点类
    """

    def __init__(self, root_node=None, left_subtree=None, right_subtree=None):
        self.root_node = root_node
        self.left_subtree = left_subtree
        self.right_subtree = right_subtree


class BinaryTree:
    """
        二叉树类
    """

    def __init__(self, node=None):
        self.node = node

    def is_empty(self):
        if not self.node:
            return True
        return False

    def pre_order(self, node):
        """
            先序遍历
        @param node:
        @return:
        """
        if not node:
            return
        print(node.root_node, end=" ")
        self.pre_order(node.left_subtree)
        self.pre_order(node.right_subtree)

    def infix_order(self, node):
        """
            中序遍历
        @param node:
        @return:
        """
        if not node:
            return
        self.infix_order(node.left_subtree)
        print(node.root_node, end=" ")
        self.infix_order(node.right_subtree)

    def post_order(self, node):
        """
            后续遍历
        @param node:
        @return:
        """
        if not node:
            return
        self.post_order(node.left_subtree)
        self.post_order(node.right_subtree)
        print(node.root_node, end=" ")

    def level_order(self):
        """
            层次遍历
        @param node:
        @return:
        """
        queue = SequenceQueue()
        queue.enqueue(self.node)
        while not queue.is_empty():
            node = queue.dequeue()
            print(node.root_node, end=" ")
            if node.left_subtree:
                queue.enqueue(node.left_subtree)
            if node.right_subtree:
                queue.enqueue(node.right_subtree)


"""
        A
    B      C
         D   E
       F G  H I
"""

if __name__ == "__main__":
    # 后序遍历增加节点 b f g d h i e c a
    b = TreeNode("B")
    f = TreeNode("F")
    g = TreeNode("G")
    d = TreeNode("D", f, g)
    h = TreeNode("H")
    i = TreeNode("I")
    e = TreeNode("E", h, i)
    c = TreeNode("C", d, e)
    a = TreeNode("A", b, c)
    binary = BinaryTree(a)
    print(binary.is_empty())
    binary.pre_order(binary.node)
    print("==========")
    binary.infix_order(binary.node)
    print("==========")
    binary.post_order(binary.node)
    print("==========")
    binary.level_order()
