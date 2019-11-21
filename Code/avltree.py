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

    def update_height(self):
        if self.is_leaf():
            self.height = 0
        elif not self.has_left():
            self.height = self.right.height + 1
        elif not self.has_right():
            self.height = self.left.height + 1
        else:
            if self.left.height > self.right.height:
                self.height = self.left.height + 1
            else:
                self.height = self.right.height + 1

    def balance_factor(self):
        if self.is_leaf():
            return 0
        elif not self.has_right():
            return -self.left.height - 1
        elif not self.has_left():
            return self.right.height + 1
        else:
            return self.right.height - self.left.height

    def right_rotate(self):
        pass

    def left_rotate(self):
        pass


class AVLTree(object):
    def __init__(self, items=None):
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def is_empty(self):
        return self.root is None

    def insert(self, item, node=None):
        if self.root is None:
            self.root = AVLNode(item)
            self.size += 1
        if node is None:
            node = self.root
            self.size += 1
        if item == node.data:
            self.size -= 1
            return
        elif item < node.data:
            # check if there is something in the nodes left spot
            if node.has_left():
                # if so recursively call insert on that node
                self.insert(item, node.left)
            # otherwise
            else:
                # add the new node to the left
                new_node = AVLNode(item)
                node.left = new_node
        else:
            # check if there is something in the nodes right spot
            if node.has_right():
                # if so recursively call insert on that node and store its subtree
                self.insert(item, node.right)
            # otherwise
            else:
                # add the new node to the right
                pass
        # update the weights of the node
        node.update_height()
        # balance the node's subtrees
        self.balance(node)

    def balance(self, node):
        pass