#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum integer values)
    minimum = float('inf')
    maximum = float('-inf')
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    # Create list of counts with a slot for each number in input range
    num_places = [0] * (maximum - minimum + 1)
    # Loop over given numbers and increment each number's count
    for num in numbers:
        num_places[num - minimum] += 1
    # Loop over counts and append that many numbers into output list
    # Improve this to mutate input instead of creating new output list
    curr_index = 0
    for num, count in enumerate(num_places):
        for _ in range(count):
            numbers[curr_index] = minimum + num
            curr_index += 1    
    return numbers

nums = [3,5,2,6,1,1,6,2,3]
sorted_nums = counting_sort(nums)
print(sorted(nums))  
    


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
