#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n) always because we have to go through each element in both arrays once
    Memory usage: O(n) because we have to create a new array that is the size of the input"""
    i1 = 0
    i2 = 0
    merged_list = []
    while i1 != len(items1) or i2 != len(items2):
        if i1 == len(items1):
            merged_list.append(items2[i2])
            i2 += 1
        elif i2 == len(items2):
            merged_list.append(items1[i1])
            i1 += 1
        elif items1[i1] < items2[i2]:
            merged_list.append(items1[i1])
            i1 += 1
        else:  # items2[i2] <= items1[i1]
            merged_list.append(items2[i2])
            i2 += 1
    return merged_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(2(n/2)^2) if the sorting algorithm takes O(n^2) time.
    This still equates to O(n) time, but as we scale it gets exponentially slower.
    For instance 4^2 = 16, but (4/2^2) = 4. 100^2 = 10000, but 50^2 = 2500
    Memory usage: ??? Why and under what conditions?"""
    # Split items list into approximately equal halves
    middle = len(items // 2)
    first_half = items[:middle]
    second_half = items[middle:]
    # Sort each half using any other sorting algorithm
    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)
    # Merge sorted halves into one list in sorted order
    merged_halves = merge(first_half, second_half)
    return merged_halves


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log(n)) because we split the list into halves taking log n time. then sort
    them using merge taking n time.
    Memory usage: also o(n(log n)) because we every time we split the array we cut it in half
    and create two new arrays of size n. This happens log(n) times."""
    # Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    # Split items list into approximately equal halves
    else:
        middle = len(items) // 2
        first_half = items[: middle]
        second_half = items[middle:]
        # Sort each half by recursively calling merge sort
        sorted_first = merge_sort(first_half)
        sorted_second = merge_sort(second_half)
        # Merge sorted halves into one list in sorted order
        return merge(sorted_first, sorted_second)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (the low) from that range, moving 
    pivot into index `p`, items less than pivot into range `[low...p-1]`, and 
    items greater than pivot into range `[p+1...high]`.
    Running time: O(n) always because we only have to go through the array once.
    We also only use swapping which takes constant time. (no inseting or deleting)
    Memory usage: O(1) because we only have to keep track of the pivot index and the
    first high index, which could also be called next low index."""
    # Choose a pivot any way and document your method in docstring above
    pivot_value = items[low]
    first_high_index = low + 1
    # Loop through all items in range [low...high]
    for index in range(1, high):
        # Move items less than pivot into front of range [low...p-1]
        if items[index] < pivot_value:
            items[first_high_index], items[index] = items[index], items[first_high_index]
            first_high_index += 1
    # Move pivot item into final position and return its position
    items[first_high_index - 1], items[low] = items[low], items[first_high_index - 1]
    return first_high_index - 1


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
