import random

comparisons = 0
swaps = 0


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    global swaps
    swaps += 1


def equals(a, b):
    global comparisons
    comparisons += 1
    return a == b


def less(a, b):
    global comparisons
    comparisons += 1
    return a < b


def select(arr, k, show=False):
    global comparisons
    global swaps
    comparisons = 0
    swaps = 0
    return __select(arr, k, 0, len(arr) - 1, show), comparisons, swaps


def random_select(arr, k, show=False):
    global comparisons
    global swaps
    comparisons = 0
    swaps = 0
    return __random_select(arr, k, 0, len(arr) - 1, show), comparisons, swaps


def __random_select(arr, k, start, end, show):
    if equals(start, end):
        return arr[start]
    pivot = random_partition(arr, start, end)
    if show:
        print(arr)
    if equals(pivot, k):
        return arr[pivot]
    elif less(k, pivot):
        return __random_select(arr, k, start, pivot - 1, show)
    else:
        return __random_select(arr, k, pivot + 1, end, show)


def __select(arr, k, start, end, show):
    if equals(start, end):
        return arr[start]
    pivot = partition(arr, start, end)
    if show:
        print(arr)
    if equals(pivot, k):
        return arr[pivot]
    elif less(k, pivot):
        return __select(arr, k, start, pivot - 1, show)
    else:
        return __select(arr, k, pivot + 1, end, show)


def random_partition(arr, start, end):
    pivot = random.randint(start, end)
    swap(arr, pivot, end)
    return partition(arr, start, end)


def partition(arr, start, end):
    pivot = arr[end]
    i = start
    for j in range(start, end):
        if not less(pivot, arr[j]):
            swap(arr, i, j)
            i += 1
    swap(arr, i, end)
    return i


def binary_search(arr, x):
    global comparisons
    comparisons = 0
    return __binary_search(arr, x, 0, len(arr) - 1)


def __binary_search(arr, x, start, end):
    if less(end, start):
        return False, comparisons
    mid = (start + end) // 2
    if equals(x, arr[mid]):
        return True, comparisons
    elif less(x, arr[mid]):
        return __binary_search(arr, x, start, mid - 1)
    else:
        return __binary_search(arr, x, mid + 1, end)

