#!python


def is_sorted(items, reverse=False, key=lambda item: item):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) because we have to go through the array once.
    Memory usage: O(1) because we only declare one variable, i"""

    # iterate through the items in the array in pairs
    for i in range(len(items) - 1):
        # check if the first item is greater than the latter
        if key(items[i]) > key(items[i + 1]) and reverse is False:
            # if so return false
            return False
        elif key(items[i]) < key(items[i + 1]) and reverse is True:
            return False
            # if we've made it through the array with no items greater than their followers return true
    return True


def bubble_sort(items, reverse=False, key=lambda item: item):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) because we have to iterate through the array n times.
    Memory usage: 1, swaps happen in place, but flags are stored"""

    # create a bool to indicate if the list is sorted
    is_sorted = False
    # keep track of the iteration so we can ignore the already sorted items
    iteration = 0
    # repeat bubble sort until items is sorted or when iterations is equal to the length of items - 1
    while not is_sorted or iteration == len(items) - 1:
        # keep track of if there is a swap (if there's no swap items is sorted)
        had_swap = False
        # iterate through the array in pairs
        for i in range(len(items) - iteration - 1):
            # check if the former item is greater
            if items[i] > items[i + 1]:
                # if so swap them
                items[i], items[i + 1] = items[i + 1], items[i]
                # set has_swap to True
                had_swap = True
        # increment iteration
        iteration += 1
        # check if no swap happened
        if not had_swap:
            # if so is_sorted is True so we can stop sorting
            is_sorted = True

    if reverse is True:
        items = items[::-1]


def selection_sort(items, reverse=False):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) always because we need to find the minimum 
    element O(n) and swap it n times.
    Memory usage: O(1) because swaps happen in place and only one
    variable, i, is created"""

    # iterate through i in the len of items to keep track of the length of the sorted part
    for i in range(len(items)):
        # find the index of the minimum element
        min_index = items[i:].index(min(items[i:])) + i
        # swap the minimum element with the first unsorted item
        items[i], items[min_index] = items[min_index], items[i]

    if reverse is True:
        items = items[::-1]


def insertion_sort(items, reverse=False):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2) because for each item (O(n)) we need to find its place 
    in the sorted array (O(n)) and then insert it (O(n)). Really 2*O(n^2).
    Memory usage: O(1) because we only keep track of the item, prev, and index."""

    # keep track of the previous item
    prev = None
    # iterate through each item in items keeping track of their index
    for i, item in enumerate(items):
        # check if prev is none
        if prev is None:
            # if so prev is item and continue
            prev = item
        # otherwise
        else:
            # check if the item is greater than the prev
            if item > prev:
                # if so set prev to item and continue
                prev = item
            # otherwise we have to find its new place in the sorted part and insert it
            else:
                # iterate through the sorted items in sorted part
                for j in range(i):
                    # if the sorted item is less than the item
                    if item < items[j]:
                        # inser the item in its position
                        items.insert(j, item)
                        # remove the item from its original position
                        items.pop(i + 1)
                        # stop looking for a position
                        break
                # set prev to the last sorted item
                prev = items[i]

    if reverse is True:
        items = items[::-1]
