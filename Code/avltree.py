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
        left_node = self.left
        self.left = left_node.right
        left_node.right = self
        self.update_height()
        left_node.update_height()
        return left_node

    def left_rotate(self):
        right_node = self.right
        self.right = right_node.left
        right_node.left = self
        self.update_height()
        right_node.update_height()
        return right_node


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
                # if so recursively call insert on that node and store its subtree
                new_subtree = self.insert(item, node.left)
                # check if a new subtree was returned by the insertion
                if new_subtree is not None:
                    # if so update its left child with the new subtree
                    node.left = new_subtree
            # otherwise
            else:
                # add the new node to the left
                new_node = AVLNode(item)
                node.left = new_node
        else:
            # check if there is something in the nodes right spot
            if node.has_right():
                # if so recursively call insert on that node and store its subtree
                new_subtree = self.insert(item, node.right)
                # check if a new subtree was returned by the insertion
                if new_subtree is not None:
                    # if so update its left child with the new subtree
                    node.right = new_subtree
            # otherwise
            else:
                # add the new node to the right
                new_node = AVLNode(item)
                node.right = new_node
        # update the weights of the node
        node.update_height()
        # balance the node's subtrees
        return self.balance(node)

    def balance(self, node):
        # get the node's balance factor
        balance_factor = node.balance_factor()
        # check if the node's subtree is balanced
        if abs(balance_factor) < 2:
            # if it is return nothing
            return None
        # check if the tree is skewed left
        if balance_factor < -1:
            # If item is less than the node.left
            if node.left.balance_factor() < 0:
                # left-left case
                new_root = node.right_rotate()
            else:  # item is greater than the node.left
                # left-right case
                node.left = node.left.left_rotate()
                new_root = node.right_rotate()
        else:  # balance factor is positive (tree skewed right)
            # If item is less than node.right.data
            if node.right.balance_factor() > 0:
                # right-right case,
                new_root = node.left_rotate()
            # if item is greater than the node.right.data
            else:
                # right-Left case
                node.right = node.right.right_rotate()
                new_root = node.left_rotate()
        # if the node is already our root
        if node is self.root:
            # update the root
            self.root = new_root
        # return the new root so the parent can update its child
        return new_root

    def items_in_order(self):
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def items_level_order(self):
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_level_order(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) because we must visit each node
        Memory usage: Worse case: O(n) if all the nodes are children of one another"""
        # Create queue to store nodes not yet traversed in level-order
        queue = deque()
        # Enqueue given starting node
        queue.append(start_node)
        # Loop until queue is empty
        while len(queue) is not 0:
            # Dequeue node at front of queue
            node = queue.popleft()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.append(node.left)
            # Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.append(node.right)

    def _traverse_in_order_recursive(self, node, visit):
        if node.has_left():
            self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
        visit(node.data)
        # Traverse right subtree, if it exists
        if node.has_right():
            self._traverse_in_order_recursive(node.right, visit)


if __name__ == '__main__':
    at = AVLTree([1, 7, 5, 8, 6, 15, 4])
