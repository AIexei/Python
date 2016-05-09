import math

def radix_sort(array):
    base = 10
    max_len = len(str(max(array)))

    for x in range(max_len):
        bins = [[] for i in range(base)]
        for y in array:
            bins[int(y / 10**x) % base].append(y)

        array = []
        for section in bins:
            array.extend(section)
    return array


def quick_sort(array):
    less = []
    pivotList = []
    more = []

    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        for i in array:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more


def merge_sort(array):
    length = len(array)

    if length >= 2:
        mid = int(length/2)
        array = __merge(merge_sort(array[:mid]), merge_sort(array[mid:]))

    return array


def __merge(left, right):
    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result.extend(left)

    if right:
        result.extend(right)

    return result

