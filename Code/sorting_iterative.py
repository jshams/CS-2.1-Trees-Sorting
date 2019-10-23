#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) because we have to go through the array once.
    TODO: Memory usage: 0 because we only look at the array"""
    for i in range(items - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) because we have to iterate through the array n times.
    Memory usage: 1, swaps happen in place, but flags are stored"""
    is_sorted = False
    iteration = 0
    while not is_sorted or iteration == len(items) - 1:
        had_swap = False
        # iterate through the array in pairs and swap them if the latter is lesser
        for i in range(len(items) - iteration - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                had_swap = True
        iteration += 1
        if not had_swap:
            is_sorted = True


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    for i in range(len(items)):
        min_index = items.index(min(items[i:]))
        items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.`
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    prev = None
    for i, item in enumerate(items):
        if prev == None:
            prev = item
        else:
            if item > prev:
                prev = item
            else:
                # find its new place in the sorted part
                for j in range(i):
                    if item < items[j]:
                        items.insert(j, item)
                        items.pop(i + 1)
                        break
                prev = items[i]
