#!python

from avltree import AVLTree, AVLNode
import unittest


class AVLTreeNodeTest(unittest.TestCase):

    def test_init(self):
        data = 123
        node = AVLNode(data)
        assert node.data is data
        assert node.left is None
        assert node.right is None

    def test_is_leaf(self):
        # Create node with no children
        node = AVLNode(2)
        assert node.is_leaf() is True
        # Attach left child node
        node.left = AVLNode(1)
        assert node.is_leaf() is False
        # Attach right child node
        node.right = AVLNode(3)
        assert node.is_leaf() is False
        # Detach left child node
        node.left = None
        assert node.is_leaf() is False
        # Detach right child node
        node.right = None
        assert node.is_leaf() is True

    def test_is_branch(self):
        # Create node with no children
        node = AVLNode(2)
        assert node.is_branch() is False
        # Attach left child node
        node.left = AVLNode(1)
        assert node.is_branch() is True
        # Attach right child node
        node.right = AVLNode(3)
        assert node.is_branch() is True
        # Detach left child node
        node.left = None
        assert node.is_branch() is True
        # Detach right child node
        node.right = None
        assert node.is_branch() is False

    def test_height(self):
        # Create node with no children
        node = AVLNode(4)
        assert node.height == 0
        # Attach left child node
        node.left = AVLNode(2)
        node.update_height()
        assert node.height == 1
        # Attach right child node
        node.right = AVLNode(6)
        node.update_height()
        assert node.height == 1
        # Attach left-left grandchild node
        node.left.left = AVLNode(1)
        node.left.update_height()
        node.update_height()
        assert node.height == 2
        # Attach right-right grandchild node
        node.right.right = AVLNode(8)
        node.right.update_height()
        node.update_height()
        assert node.height == 2
        # Attach right-right-left great-grandchild node
        node.right.right.left = AVLNode(7)
        node.right.right.update_height()
        node.right.update_height()
        node.update_height()
        assert node.height == 3


class AVLTreeTest(unittest.TestCase):

    def test_init(self):
        tree = AVLTree()
        assert tree.root is None
        assert tree.size == 0
        assert tree.is_empty() is True

    def test_init_with_list(self):
        tree = AVLTree([2, 1, 3])
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right.data == 3
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_init_with_list_of_strings(self):
        tree = AVLTree(['B', 'A', 'C'])
        assert tree.root.data == 'B'
        assert tree.root.left.data == 'A'
        assert tree.root.right.data == 'C'
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_init_with_list_of_tuples(self):
        tree = AVLTree([(2, 'B'), (1, 'A'), (3, 'C')])
        assert tree.root.data == (2, 'B')
        assert tree.root.left.data == (1, 'A')
        assert tree.root.right.data == (3, 'C')
        assert tree.size == 3
        assert tree.is_empty() is False

    def test_size(self):
        tree = AVLTree()
        assert tree.size == 0
        tree.insert('B')
        assert tree.size == 1
        tree.insert('A')
        assert tree.size == 2
        tree.insert('C')
        assert tree.size == 3

    def test_insert_with_3_items(self):
        # Create a complete binary search tree of 3 items in level-order
        tree = AVLTree()
        tree.insert(2)
        assert tree.root.data == 2
        assert tree.root.left is None
        assert tree.root.right is None
        tree.insert(1)
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right is None
        tree.insert(3)
        assert tree.root.data == 2
        assert tree.root.left.data == 1
        assert tree.root.right.data == 3

    def test_insert_with_7_items(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = AVLTree()
        for item in items:
            tree.insert(item)
        assert tree.root.data == 4
        assert tree.root.left.data == 2
        assert tree.root.right.data == 6
        assert tree.root.left.left.data == 1
        assert tree.root.left.right.data == 3
        assert tree.root.right.left.data == 5
        assert tree.root.right.right.data == 7

    def test_items_in_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = AVLTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == ['A', 'B', 'C']

    def test_items_level_order_with_3_strings(self):
        # Create a complete binary search tree of 3 strings in level-order
        items = ['B', 'A', 'C']
        tree = AVLTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == ['B', 'A', 'C']

    def test_items_in_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = AVLTree(items)
        # Ensure the in-order traversal of tree items is ordered correctly
        assert tree.items_in_order() == [1, 2, 3, 4, 5, 6, 7]

    def test_items_level_order_with_7_numbers(self):
        # Create a complete binary search tree of 7 items in level-order
        items = [4, 2, 6, 1, 3, 5, 7]
        tree = AVLTree(items)
        # Ensure the level-order traversal of tree items is ordered correctly
        assert tree.items_level_order() == [4, 2, 6, 1, 3, 5, 7]


if __name__ == '__main__':
    unittest.main()
