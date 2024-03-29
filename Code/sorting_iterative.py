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
    items_is_sorted = False
    # keep track of the iteration so we can ignore the already sorted items
    iteration = 1
    # repeat bubble sort until items is sorted or when iterations is equal to the length of items - 1
    while not items_is_sorted or iteration == len(items):
        # keep track of if there is a swap (if there's no swap items is sorted)
        had_swap = False
        # iterate through the array in pairs
        for i in range(len(items) - iteration):
            # check if the former item is greater
            if key(items[i]) > key(items[i + 1]):
                # if so swap them
                items[i], items[i + 1] = items[i + 1], items[i]
                # set has_swap to True
                had_swap = True
        # increment iteration
        iteration += 1
        # check if no swap happened
        if not had_swap:
            # if so items_is_sorted is True so we can stop sorting
            items_is_sorted = True

    if reverse is True:
        items[::] = items[::-1]


def cocktail_shaker_sort(items, reverse=False, key=lambda item: item):
    '''Sorts items similar to bubble sort (swapping adjacent items that are out 
    of order) but in this algorithm we change between going forwards through
    items, or backwards every iteration.
    So after the first iteration the last item is sorted, and after the second
    the first and last items will be sorted and so on.
    Running time: O(n^2) because we have to iterate through the array n times.
    Memory usage: O(1) because swaps happen in place.'''
    start = 1
    end = len(items)
    step = 1
    for _ in range(end):
        for i in range(start, end, step):
            if key(items[i]) < key(items[i - 1]):
                items[i], items[i - 1] = items[i - 1], items[i]
        end, start = start - step, end - 2 * step
        step = -step
    if reverse is True:
        items[::] = items[::-1]


def selection_sort(items, reverse=False, key=lambda item: item):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) always because we need to find the minimum 
    element O(n) and swap it n times.
    Memory usage: O(1) because swaps happen in place and only one
    variable, i, is created"""

    # iterate through i in the len of items to keep track of the length of the sorted part
    for i in range(len(items)):
        # find the index of the minimum element
        min_index = items[i:].index(min(items[i:], key=key)) + i
        # swap the minimum element with the first unsorted item
        items[i], items[min_index] = items[min_index], items[i]

    if reverse is True:
        items[::] = items[::-1]


def find_insert_location(items, item, end, key=lambda item: item, start=0):
    '''input: items - a list of items, item - the item we want to insert
    end - the first unsorted index of items, or the last sorted index not inclusive
    start - default 0, used for
    recursively finding the index.
    Using binary search recursively find the index to insert item in items'''
    # print(start, end)
    if (end - start) <= 1:
        if key(item) < key(items[start]):
            return start
        else:
            return start + 1
    middle = (start + end) // 2
    if key(item) < key(items[middle]):
        return find_insert_location(items, item, middle, key, start)
    else:
        return find_insert_location(items, item, end, key, middle)


def insertion_sort(items, reverse=False, key=lambda item: item):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2) because for each item (O(n)) we need to find its place 
    in the sorted array (O(logn)) and then insert it (O(n)). Really O(n^2 * logn).
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
            #
            if key(item) > key(prev):
                # if so set prev to item and continue
                prev = item
            # otherwise we have to find its new place in the sorted part and insert it
            else:
                insert_location = find_insert_location(items, item, i, key)
                # remove it from its previous location
                items.pop(i)
                # insert it in its new location
                items.insert(insert_location, item)
                # set prev to the last sorted item
                prev = items[i]

    if reverse is True:
        items[::] = items[::-1]
