#!python3

from auto_complete import Trie as PrefixTree
from auto_complete import DictNode as PrefixTreeNode
import unittest


class PrefixTreeTest(unittest.TestCase):

    def test_init_and_properties(self):
        tree = PrefixTree()
        # Verify tree size property
        # assert isinstance(tree.size, int)
        assert tree.size == 0
        # Verify root node
        # assert isinstance(tree.root, PrefixTreeNode)
        assert tree.root.character == '^'
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 0

    def test_init_with_string(self):
        tree = PrefixTree(['a'])
        # Verify root node
        assert tree.root.character == '^'
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 1
        assert tree.root.has_child('a') is True
        # Verify node 'a'
        node_a = tree.root.get_child('a')
        assert node_a.character == 'a'
        assert node_a.is_terminal() is True
        assert node_a.num_children() == 0

    def test_insert_with_string(self):
        tree = PrefixTree()
        tree.insert('ab')
        # Verify root node
        assert tree.root.character == '^'
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 1
        assert tree.root.has_child('a') is True
        # Verify node 'a'
        node_a = tree.root.get_child('a')
        assert node_a.character == 'a'
        assert node_a.is_terminal() is False
        assert node_a.num_children() == 1
        assert node_a.has_child('b') is True
        # Verify node 'b'
        node_b = node_a.get_child('b')
        assert node_b.character == 'b'
        assert node_b.is_terminal() is True
        assert node_b.num_children() == 0

    def test_insert_with_4_strings(self):
        tree = PrefixTree()
        # Insert new string that starts from root node
        tree.insert('abc')
        # Verify root node
        assert tree.root.character == '^'
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 1
        assert tree.root.has_child('a') is True
        # Verify new node 'a'
        node_a = tree.root.get_child('a')
        assert node_a.character == 'a'
        assert node_a.is_terminal() is False
        assert node_a.num_children() == 1
        assert node_a.has_child('b') is True
        # Verify new node 'b'
        node_b = node_a.get_child('b')
        assert node_b.character == 'b'
        assert node_b.is_terminal() is False
        assert node_b.num_children() == 1
        assert node_b.has_child('c') is True
        # Verify new node 'c'
        node_c = node_b.get_child('c')
        assert node_c.character == 'c'
        assert node_c.is_terminal() is True
        assert node_c.num_children() == 0

        # Insert string with partial overlap so node 'b' has new child node 'd'
        tree.insert('abd')
        # Verify root node again
        assert tree.root.character == '^'
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 1
        assert tree.root.has_child('a') is True
        # Verify node 'a' again
        assert node_a.character == 'a'
        assert node_a.is_terminal() is False
        assert node_a.num_children() == 1
        assert node_a.has_child('b') is True
        # Verify node 'b' again
        assert node_b.character == 'b'
        assert node_b.is_terminal() is False
        assert node_b.num_children() == 2  # Node 'b' now has two children
        assert node_b.has_child('c') is True  # Node 'c' is still its child
        assert node_b.has_child('d') is True  # Node 'd' is its new child
        # Verify new node 'd'
        node_d = node_b.get_child('d')
        assert node_d.character == 'd'
        assert node_d.is_terminal() is True
        assert node_d.num_children() == 0

        # Insert substring already in tree so node 'a' becomes terminal
        tree.insert('a')
        # Verify root node again
        assert tree.root.character == '^'
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 1
        assert tree.root.has_child('a') is True
        # Verify node 'a' again
        assert node_a.character == 'a'
        assert node_a.is_terminal() is True  # Node 'a' is now terminal
        assert node_a.num_children() == 1  # Node 'a' still has one child
        assert node_a.has_child('b') is True  # Node 'b' is still its child

        # Insert new string with no overlap that starts from root node
        tree.insert('xyz')
        # Verify root node again
        assert tree.root.character == '^'
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 2  # Root node now has two children
        assert tree.root.has_child('a') is True  # Node 'a' is still its child
        assert tree.root.has_child('x') is True  # Node 'x' is its new child
        # Verify new node 'x'
        node_x = tree.root.get_child('x')
        assert node_x.character == 'x'
        assert node_x.is_terminal() is False
        assert node_x.num_children() == 1
        assert node_x.has_child('y') is True
        # Verify new node 'y'
        node_y = node_x.get_child('y')
        assert node_y.character == 'y'
        assert node_y.is_terminal() is False
        assert node_y.num_children() == 1
        assert node_y.has_child('z') is True
        # Verify new node 'z'
        node_z = node_y.get_child('z')
        assert node_z.character == 'z'
        assert node_z.is_terminal() is True
        assert node_z.num_children() == 0

    def test_size_and_is_empty(self):
        tree = PrefixTree()
        # Verify size after initializing tree
        assert tree.size == 0
        assert tree.is_empty() is True
        # Verify size after first insert
        tree.insert('a')
        assert tree.size == 1
        assert tree.is_empty() is False
        # Verify size after second insert
        tree.insert('abc')
        assert tree.size == 2
        assert tree.is_empty() is False
        # Verify size after third insert
        tree.insert('abd')
        assert tree.size == 3
        assert tree.is_empty() is False
        # Verify size after fourth insert
        tree.insert('xyz')
        assert tree.size == 4
        assert tree.is_empty() is False

    def test_size_with_repeated_insert(self):
        tree = PrefixTree()
        # Verify size after initializing tree
        assert tree.size == 0
        assert tree.is_empty() is True
        # Verify size after first insert
        tree.insert('a')
        assert tree.size == 1
        assert tree.is_empty() is False
        # Verify size after repeating first insert
        tree.insert('a')
        assert tree.size == 1
        # Verify size after second insert
        tree.insert('abc')
        assert tree.size == 2
        # Verify size after repeating second insert
        tree.insert('abc')
        assert tree.size == 2
        # Verify size after third insert
        tree.insert('abd')
        assert tree.size == 3
        # Verify size after repeating third insert
        tree.insert('abd')
        assert tree.size == 3
        # Verify size after fourth insert
        tree.insert('xyz')
        assert tree.size == 4
        # Verify size after repeating fourth insert
        tree.insert('xyz')
        assert tree.size == 4

    def test_contains(self):
        strings = ['abc', 'abd', 'a', 'xyz']
        tree = PrefixTree(strings)
        # Verify contains for all substrings
        assert tree.contains('abc') is True
        assert tree.contains('abd') is True
        assert tree.contains('ab') is False
        assert tree.contains('bc') is False
        assert tree.contains('bd') is False
        assert tree.contains('a') is True
        assert tree.contains('b') is False
        assert tree.contains('c') is False
        assert tree.contains('d') is False
        assert tree.contains('xyz') is True
        assert tree.contains('xy') is False
        assert tree.contains('yz') is False
        assert tree.contains('x') is False
        assert tree.contains('y') is False
        assert tree.contains('z') is False

    def test_complete(self):
        strings = ['abc', 'abd', 'a', 'xyz']
        tree = PrefixTree(strings)
        # Verify completions for all substrings
        assert tree.auto_complete('abc') == ['abc']
        assert tree.auto_complete('abd') == ['abd']
        assert tree.auto_complete('ab') == ['abc', 'abd']
        assert tree.auto_complete('bc') == []
        assert tree.auto_complete('bd') == []
        assert tree.auto_complete('a') == ['a', 'abc', 'abd']
        assert tree.auto_complete('b') == []
        assert tree.auto_complete('c') == []
        assert tree.auto_complete('d') == []
        assert tree.auto_complete('xyz') == ['xyz']
        assert tree.auto_complete('xy') == ['xyz']
        assert tree.auto_complete('yz') == []
        assert tree.auto_complete('x') == ['xyz']
        assert tree.auto_complete('y') == []
        assert tree.auto_complete('z') == []

    def test_strings(self):
        tree = PrefixTree()
        input_strings = []  # Strings that have been inserted into the tree
        for string in ['abc', 'abd', 'a', 'xyz']:  # Strings to be inserted
            # Insert new string and add to list of strings already inserted
            tree.insert(string)
            input_strings.append(string)
            # Verify tree can retrieve all strings that have been inserted
            tree_strings = tree.strings()
            assert len(tree_strings) == len(input_strings)  # check length only
            self.assertCountEqual(tree_strings, input_strings)  # Ignore order


if __name__ == '__main__':
    unittest.main()
