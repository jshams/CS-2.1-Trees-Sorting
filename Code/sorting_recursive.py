#!python
from random import randint


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
    else:
        # Split items list into approximately equal halves
        middle = len(items) // 2
        first_half = items[: middle]
        second_half = items[middle:]
        # Sort each half by recursively calling merge sort
        sorted_first = merge_sort(first_half)
        sorted_second = merge_sort(second_half)
        # Merge sorted halves into one list in sorted order
        return merge(sorted_first, sorted_second)


def find_median(items, i1, i2, i3):
    '''Input a list of items and three indicies
    returns the index whose value in items is in the middle'''
    if items[i1] > items[i2]:
        if items[i2] > items[i3]:
            return i2
        else:  # i2 < i1 and i2 < i3
            if items[i1] > items[i3]:
                return i3
            else:  # i2 < i1 < i3
                return i1
    else:  # i1 < i2
        if items[i1] > items[i3]:
            return i1
        else:  # i1 < i3 and i1 < i2
            if items[i2] > items[i3]:
                return i3
            else:  # i1 < i2 < i3
                return i2


def partition(items, low, high, pivot_method="first"):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (the low) from that range, moving
    pivot into index `p`, items less than pivot into range `[low...p-1]`, and
    items greater than pivot into range `[p+1...high]`.
    pivot_index param:
    "first" - (default) will chose the frist index as the pivot
    "last" - will chose the last index [-1] as the pivot
    "middle" - will chose the middle index as the pivot
    "random" - will chose a random index as the pivot
    "outer middle" - will look at the first, middle, and last items in the arr and
    take the median of the three
    "smart random" - will look at three random values and use their median as the pivot
    Running time: O(n) always because we only have to go through the array once.
    We also only use swapping which takes constant time. (no inseting or deleting)
    Memory usage: O(1) because we only have to keep track of the pivot index and the
    first high index, which could also be called next low index."""
    # Depending on the parameter passed in chose a pivot using that method
    if pivot_method == 'last':
        items[high - 1], items[low] = items[low], items[high - 1]
    elif pivot_method == 'middle':
        middle_index = (low + high) // 2
        items[middle_index], items[low] = items[low], items[middle_index]
    elif pivot_method == 'random':
        random_index = randint(low, high-1)
        items[random_index], items[low] = items[low], items[random_index]
    elif pivot_method == 'outer middle':
        median_index = find_median(items, low, (low + high) // 2, high-1)
        items[median_index], items[low] = items[low], items[median_index]
    elif pivot_method == 'smart random':
        i1, i2, i3 = randint(low, high-1), randint(low,
                                                   high-1), randint(low, high-1)
        pivot_index = find_median(items, i1, i2, i3)
        items[pivot_index], items[low] = items[low], items[pivot_index]

    pivot_value = items[low]
    first_high_index = low + 1
    # Loop through all items in range [low...high]
    for index in range(low + 1, high):
        # Move items less than pivot into front of range [low...p-1]
        if items[index] < pivot_value:
            items[first_high_index], items[index] = items[index], items[first_high_index]
            first_high_index += 1
    # Move pivot item into final position and return its position
    items[first_high_index - 1], items[low] = items[low], items[first_high_index - 1]
    return first_high_index - 1


def quick_sort(items, low=0, high=None, pivot_method="first"):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(n*log(n)). The input looks weird, but lists that are more
    shuffled or random will sort quicker.
    Worst case running time: O(n^2) if the list is in sorted or reverse sorted order.
    Best case memory usage: O(log(n)) memory is consant on each iteration and best case
    takes log(n) iterations
    Worse case memory usage: O(n) when the most iterations occur, list is sorted."""
    # Check if high and low range bounds have default values (not given)
    if high is None:
        high = len(items)
    # Check if list or range is so small it's already sorted (base case)
    if high - low <= 1:
        return
    # Partition items in-place around a pivot and get index of pivot
    pivot_index = partition(items, low, high, pivot_method)
    # Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, pivot_index, pivot_method)
    quick_sort(items, pivot_index + 1, high, pivot_method)


def bogo_sort(items):
    '''O(n!)'''
    for perm in get_all_perms(items):
        print('what')
        if sorted(perm) == perm:
            return perm


def get_all_perms(array):
    if len(array) < 2:
        return array
    if len(array) == 2:     # base case
        return [array, [array[1], array[0]]]
    all_perms = []
    for i in array:
        new_array = array[:]
        new_array.remove(i)
        all_perms_extension = get_all_perms(new_array)
        for group in all_perms_extension:
            group.insert(0, i)
        all_perms.extend(all_perms_extension)
    return all_perms


if __name__ == '__main__':
    from random import randint
    from sys import argv
    from time import time
    args = argv[1:]
    sort = quick_sort
    n = 10
    if len(args) > 0:
        n = int(args[0])
    if len(args) > 1:
        if args[1] in 'merge sort merge sort':
            sort = merge_sort
        else:
            sort = quick_sort
    items = [randint(0, n ** 2) for _ in range(n)]
    if n < 100:
        print('Unsorted items:')
        print(items)
        sort(items)
        print()
        print('Sorted items:')
        print(items)
    else:
        start = time()
        sort(items)
        finish = time()
        total = round(finish - start, ndigits=4)
        print('It only took', total, 'seconds!')
