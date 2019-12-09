#!python3

from auto_complete import DictNode, ListNode
import unittest

# change this to test DictNode or ListNode
PrefixTreeNode = DictNode

class PrefixTreeNodeTest(unittest.TestCase):

    def test_init_and_properties(self):
        character = 'a'
        node = PrefixTreeNode(character)
        # Verify node character
        assert isinstance(node.character, str)
        assert node.character is character
        # Verify children nodes structure
        # assert isinstance(node.children, PrefixTreeNode.CHILDREN_TYPE)
        assert node.num_children() == 0
        # assert node.children == PrefixTreeNode.CHILDREN_TYPE()
        # Verify terminal boolean
        assert isinstance(node.terminal, bool)
        assert node.terminal is False

    def test_child_methods(self):
        # Create node 'A' and verify it does not have any children
        node_A = PrefixTreeNode('a')
        assert node_A.num_children() == 0
        assert node_A.has_child('b') is False
        # Verify getting child from node 'A' raises error
        with self.assertRaises(ValueError):
            node_A.get_child('b')
        # Create node 'B' and add it as child to node 'A'
        node_A.add_child('b')
        node_B = node_A.get_child('b')
        # Verify node 'A' has node 'B' as child
        assert node_A.num_children() == 1
        assert node_A.has_child('b') is True
        assert node_A.get_child('b') is node_B
        # Verify adding node 'B' as child to node 'A' again raises error
        with self.assertRaises(ValueError):
            node_A.add_child('b')
        # Create node 'C' and add it as another child to node 'A'
        node_A.add_child('c')
        node_C = node_A.get_child('c')
        # Verify node 'A' has both nodes 'B' and 'C' as children
        assert node_A.num_children() == 2
        assert node_A.has_child('b') is True
        assert node_A.has_child('c') is True
        assert node_A.get_child('c') is node_C
        # Verify adding node 'C' as child to node 'A' again raises error
        with self.assertRaises(ValueError):
            node_A.add_child('c')
