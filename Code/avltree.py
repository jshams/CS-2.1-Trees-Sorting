from collections import deque


class AVLNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return 'AvlNode({!r})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data

    def is_leaf(self):
        return self.left is None and self.right is None

    def is_branch(self):
        return not self.is_leaf()

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


class AVLTree(object):
    def __init__(self, items=None):
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def is_empty(self):
        return self.root is None

    def insert(self, item):
        pass
