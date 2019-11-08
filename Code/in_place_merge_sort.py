from random import randint


def in_place_merge_sort(items, start=None, end=None):
    if start is None and end is None:
        start, end = 0, len(items) - 1
    if end - start <= 1:
        pass
    else:
        middle = start + end // 2
        in_place_merge_sort(items, start, middle)
        in_place_merge_sort(items, middle, end)

        in_place_merge(items, start, middle, end)


def print_info(items, i1, i2, i, middle):
    output = '['
    for index, item in enumerate(items):
        flag = 0
        if index == i1 or index == i2:
            output += '\033[94m'
            flag += 1
        if index == i:
            output += '\033[4m'
            flag += 1
        output += str(item)
        output += flag * '\033[0m'
        output += ', '
    output = output[:-2] + ']'
    print(f'i1 = {i1} i2 = {i2} i = {i}')
    print(output)


def in_place_merge(items, start, middle, end):
    i1 = start
    i2 = middle
    for i in range(start, end):
        if i1 < i:
            print('end! i1 > i')
            if items[-2] > items[-1]:
                items[-1], items[-2] = items[-2], items[-1]
            return
        print()
        print_info(items, i1, i2, i, middle)
        if i2 == end:
            if items[i1] < items[i]:
                items[i1], items[i] = items[i], items[i1]
        elif items[i1] < items[i2]:
            print(f'{items[i1]} is less than {items[i2]} (i1 < i2)')
            print(f'{items[i]} is swapped with {items[i1]}')
            items[i], items[i1] = items[i1], items[i]
            if i2 - i1 != 1:
                i1 += 1
            else:
                if i1 == i:
                    i1 += 1
                    if items[i2] < items[i]:
                        items[i2], items[i] = items[i], items[i2]
        else:  # items[i2] <= items[i1]
            print(f'{items[i2]} is less than {items[i1]} (i2 < i1)')
            print(f'{items[i]} is swapped with {items[i2]}')
            items[i], items[i2] = items[i2], items[i]
            # if i1 < middle:
            if i1 < middle:
                i1 = i2
            elif i1 == i:
                i1 = i2
            i2 += 1
    if items[-2] > items[-1]:
        items[-1], items[-2] = items[-2], items[-1]
    print(f'{items} i1 = {i1} i2 = {i2} i = {i}')


# items = [9, 10, 16, 24, 64, 4, 5, 7, 65, 100]
# items = [5, 6, 7, 8, 100, 0, 1, 2, 3, 4]


def in_place_merge_2(items, start, middle, end):
    i1 = start
    i2 = middle
    for i in range(start, end):
        print()
        print_info(items, i1, i2, i, middle)
        if i1 < i:
            # #     print('end! i1 < i')
            # if items[end - 2] > items[end - 1]:
            #     items[end - 1], items[end - 2] = items[end - 2], items[end - 1]
            # print('end', i1, i)
            # return
            print('i1 < i', i1, '<', i)
        elif i2 == end:
            items[i], items[i1] = items[i1], items[i]
            if i1 == end - 1:
                continue
            elif i1 - middle > 0:
                print('this happened')
                i1 = end - (i1 - middle)
            else:
                i1 += 1
        elif items[i] < items[i1] and items[i] < items[i2]:
            continue
        elif items[i1] <= items[i2]:  # i1 swaps with i
            print(f'{items[i1]} is less than {items[i2]} (i1 < i2)')
            print(f'{items[i]} is swapped with {items[i1]}')
            items[i], items[i1] = items[i1], items[i]
            if i1 - i == 1:
                continue
            elif i2 - i1 != 1:
                i1 += 1
            elif i1 > middle and i1 != middle and i1 - 1 != i:
                i1 -= 1

        else:  # i2 swaps with i
            print(f'{items[i2]} is less than {items[i1]} (i2 < i1)')
            print(f'{items[i]} is swapped with {items[i2]}')
            items[i], items[i2] = items[i2], items[i]
            # if i1 < middle:
            if i1 == i:
                i1 = i2
            i2 += 1
    if items[-2] > items[-1]:
        items[-1], items[-2] = items[-2], items[-1]
    print(f'{items} i1 = {i1} i2 = {i2} i = {i}')


def test(n, merge):
    first = sorted([randint(0, 100) for _ in range(n // 2)])
    second = sorted([randint(0, 100) for _ in range(n // 2)])
    items = first + second
    # items = [33, 70, 70, 91, 98, 10, 32, 43, 48, 51]
    # items = [9, 18, 52, 66, 97, 9, 23, 75, 96, 99]
    # items = [38, 68, 70, 78, 99, 7, 40, 49, 50, 61]
    # items = [13, 49, 54, 65, 96, 19, 24, 40, 73, 79]
    # items = [3, 37, 37, 43, 48, 5, 15, 32, 60, 64]
    # items = [43, 47, 70, 78, 88, 1, 44, 76, 85, 89]
    # items = [35, 40, 71, 73, 98, 18, 37, 65, 71, 81]
    # items = [(item, 'l' + str(i % (n//2)) if i // (n//2) == 0 else 'r' + str(i % (n//2)))
    #          for i, item in enumerate(items)]
    print(items)
    merge(items, 0, n // 2, n)
    print()
    print(items)
    print(sorted(items) == items)


test(6, in_place_merge_2)
