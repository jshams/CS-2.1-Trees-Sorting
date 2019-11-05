#!python

from sorting import random_ints
from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort, cocktail_shaker_sort
from sorting_recursive import split_sort_merge, merge_sort, quick_sort
from sorting_integer import counting_sort, bucket_sort
import unittest
from inspect import getfullargspec


class IsSortedTest(unittest.TestCase):

    def test_is_sorted_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert is_sorted([]) is True  # Empty lists are vacuously sorted
        assert is_sorted([3]) is True  # Single item is trivially sorted
        assert is_sorted([3, 3]) is True  # Duplicate items are in order
        assert is_sorted([3, 5]) is True
        assert is_sorted([3, 5, 7]) is True
        assert is_sorted([-5, 0, 5]) is True
        assert is_sorted([-10, -3, 0, 4, 4, 7])

    def test_is_sorted_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        assert is_sorted([5, 3]) is False
        assert is_sorted([3, 5, 3]) is False
        assert is_sorted([7, 5, 3]) is False
        assert is_sorted([10, -4, 12, 0]) is False
        assert is_sorted([12, 11, 10, 9, 8, 7]) is False

    def test_is_sorted_on_sorted_strings(self):
        # Positive test cases (examples) with lists of sorted strings
        assert is_sorted(['A']) is True  # Single item is trivially sorted
        assert is_sorted(['A', 'A']) is True  # Duplicate items are in order
        assert is_sorted(['A', 'B']) is True
        assert is_sorted(['A', 'B', 'C']) is True
        assert is_sorted(['Argentina', 'Denmark', 'Japan']) is True
        assert is_sorted(['ape', 'giraffe', 'monkey', 'zebra']) is True

    def test_is_sorted_on_unsorted_strings(self):
        # Negative test cases (counterexamples) with lists of unsorted strings
        assert is_sorted(['B', 'A']) is False
        assert is_sorted(['A', 'B', 'A']) is False
        assert is_sorted(['C', 'B', 'A']) is False
        assert is_sorted(['China', 'Algeria', 'Switzerland']) is False
        assert is_sorted(['dog', 'cat', 'elephant']) is False

    def test_is_sorted_on_sorted_tuples(self):
        # Positive test cases (examples) with lists of sorted tuples
        assert is_sorted([(3, 5)]) is True  # Single item
        assert is_sorted([(3, 'A')]) is True  # Single item
        assert is_sorted([('A', 3)]) is True  # Single item
        assert is_sorted([('A', 'B')]) is True  # Single item
        assert is_sorted([(3, 5), (3, 5)]) is True  # Duplicate items
        assert is_sorted([(3, 'A'), (3, 'A')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('A', 3)]) is True  # Duplicate items
        assert is_sorted([('A', 'B'), ('A', 'B')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('B', 5)]) is True  # Both items sorted
        assert is_sorted([('A', 3), ('B', 3)]) is True  # First item sorted
        assert is_sorted([('A', 3), ('A', 5)]) is True  # Second item sorted
        assert is_sorted([(3, 'A'), (5, 'B')]) is True  # Both items sorted
        assert is_sorted([(3, 'A'), (5, 'A')]) is True  # First item sorted
        assert is_sorted([(3, 'A'), (3, 'B')]) is True  # Second item sorted

    def test_is_sorted_on_unsorted_tuples(self):
        # Negative test cases (counterexamples) with lists of unsorted tuples
        assert is_sorted([(5, 'B'), (3, 'A')]) is False  # Both items unsorted
        assert is_sorted([(5, 'A'), (3, 'B')]) is False  # First item unsorted
        assert is_sorted([(3, 'B'), (3, 'A')]) is False  # Second item unsorted
        assert is_sorted([('B', 5), ('A', 3)]) is False  # Both items unsorted
        assert is_sorted([('B', 3), ('A', 5)]) is False  # First item unsorted
        assert is_sorted([('A', 5), ('A', 3)]) is False  # Second item unsorted

    def test_is_sorted_with_reversed_on_sorted(self):
        assert is_sorted([9, 7, 5, 3], reverse=True) is True
        assert is_sorted([9, 9, 7, 5, 4], reverse=True) is True
        # TODO: add more tests to make this more robust

    def test_is_sorted_with_reversed_on_unsorted(self):
        assert is_sorted([9, 10, 11, 12], reverse=True) is False
        assert is_sorted([1, 5, 3, 7, 9], reverse=True) is False
        # TODO: add more tests to make this more robust

    def test_is_sorted_with_key_on_sorted(self):
        def second_int(items_tuple): return items_tuple[1]
        items = [(10, 1, 5), (1, 2, 90), (30, 3, 5), (300, 4, 12)]
        assert is_sorted(items, key=second_int) is True
        # TODO: add more tests to make this more robust

    def test_is_sorted_with_key_on_unsorted(self):
        def second_int(items_tuple): return items_tuple[1]
        items = [(1, 2, 3), (1, 3, 3), (1, 1, 3), (5, 21, 90)]
        assert is_sorted(items, key=second_int) is False
        # TODO: add more tests to make this more robust

    def test_is_sorted_with_key_and_reversed_on_sorted(self):
        pass

    def test_is_sorted_with_key_and_reversed_on_unsorted(self):
        pass


class IntegerSortTest(unittest.TestCase):

    def test_sort_on_empty_list(self):
        items = []
        sort(items)
        assert items == []  # List should not be changed

    def test_sort_on_small_lists_of_integers(self):
        items1 = [3]
        sort(items1)
        assert items1 == [3]  # List should not be changed
        items2 = [5, 3]
        sort(items2)
        assert items2 == [3, 5]  # List should be in sorted order
        items3 = [5, 7, 3]
        sort(items3)
        assert items3 == [3, 5, 7]
        items4 = [5, 2, 1, 6]
        sort(items4)
        assert items4 == [1, 2, 5, 6]

    def test_sort_on_small_lists_of_integers_with_duplicates(self):
        items1 = [3, 3]
        sort(items1)
        assert items1 == [3, 3]  # List should not be changed
        items2 = [3, 5, 3]
        sort(items2)
        assert items2 == [3, 3, 5]  # List should be in sorted order
        items3 = [5, 5, 3, 5, 3]
        sort(items3)
        assert items3 == [3, 3, 5, 5, 5]
        items4 = [7, 5, 3, 7, 5, 7, 5, 3, 7]
        sort(items4)
        assert items4 == [3, 3, 5, 5, 5, 7, 7, 7, 7]
        items5 = [1, 1, 1, 1]
        sort(items5)
        assert items5 == [1, 1, 1, 1]

    def test_sort_on_lists_of_random_integers(self):
        # Generate list of 10 random integers from range [1...20]
        items1 = random_ints(10, 1, 20)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 20 random integers from range [1...50]
        items2 = random_ints(20, 1, 50)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 30 random integers from range [1...100]
        items3 = random_ints(30, 1, 100)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3

    def test_sort_on_lists_of_random_integers_with_duplicates(self):
        # Generate list of 20 random integers from range [1...10]
        items1 = random_ints(20, 1, 10)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 50 random integers from range [1...20]
        items2 = random_ints(50, 1, 20)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 100 random integers from range [1...30]
        items3 = random_ints(100, 1, 30)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3

    def test_sort_with_reverse_true(self):
         # this allows me to check if sort has a 'reverse' argument
        arguments = getfullargspec(sort).args
        if 'reverse' not in arguments:
            return
        items = random_ints(50, 1, 20)
        reverse_sorted_items = sorted(items, reverse=True)
        sort(items, reverse=True)
        assert items == reverse_sorted_items

    def test_sort_with_custom_key(self):
        # this allows me to check if sort has a 'key' argument
        arguments = getfullargspec(sort).args
        if 'key' not in arguments:
            return

        def second_int(items_tuple): return items_tuple[1]
        items1 = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
        sort(items1, key=second_int)
        assert items1 == [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)]
        items2 = [(100, 11), (12, 3), (11, 0), (120, -10)]
        sort(items2, key=sum)
        assert items2 == [(11, 0), (12, 3), (120, -10), (100, 11)]
        items3 = [(1, 5, 1, 0), (1, 3, -4, 1), (10, 22, 40)]
        sort(items3, key=min)
        assert items3 == [(1, 3, -4, 1), (1, 5, 1, 0), (10, 22, 40)]

    def test_sort_with_custom_key_and_reversed_true(self):
        arguments = getfullargspec(sort).args
        if 'key' not in arguments:
            return
        pass


class StringSortTest(unittest.TestCase):

    def test_sort_on_small_lists_of_strings(self):
        items1 = ['A']
        sort(items1)
        assert items1 == ['A']  # List should not be changed
        items2 = ['B', 'A']
        sort(items2)
        assert items2 == ['A', 'B']  # List should be in sorted order
        items3 = ['B', 'C', 'A']
        sort(items3)
        assert items3 == ['A', 'B', 'C']
        # TODO: Write more test cases with assert equal list statements
        # You'll need a lot more than this to test sorting algorithm robustness
        # ...

    def test_sort_on_fish_book_title(self):
        items = 'one fish two fish red fish blue fish'.split()
        sorted_items = sorted(items)  # Create a copy of list in sorted order
        sort(items)  # Call mutative sort function to sort list items in place
        assert items == sorted_items

    def test_sort_on_seven_dwarf_names(self):
        items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
        sorted_items = sorted(items)  # Copy
        sort(items)  # Mutate
        assert items == sorted_items


def get_sort_function():
    """Read command-line argument and return sort function with that name."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort_function'.format(script))
        print('Example: {} bubble_sort'.format(script))
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
            return sort_function
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if 'sort' in name:
                    print('    {}'.format(name))
            return


# If using PyTest, change this variable to the sort function you want to test
sort = cocktail_shaker_sort

if sort == merge_sort:
    def impure_merge_sort(items):
        sorted_items = merge_sort(items)
        items[::] = sorted_items

    sort = impure_merge_sort


if __name__ == '__main__':
    # Get sort function from command-line argument
    # FIXME: This is causing unittest to throw an error
    # sort = get_sort_function()
    unittest.main()
