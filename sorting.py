

def partition(arr, low, high):
    comparisons = 0
    shifts = 0
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            shifts += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    shifts += 1
    return i + 1, comparisons, shifts


def quickSort(arr, low, high, show=False):
    comparisons = 0
    shifts = 0
    if len(arr) == 1:
        return arr
    if low < high:
        pi, c, s = partition(arr, low, high)
        comparisons += c
        shifts += s
        if show:
            print(arr)
        c, s = quickSort(arr, low, pi - 1, show)
        comparisons += c
        shifts += s
        c, s = quickSort(arr, pi + 1, high, show)
        comparisons += c
        shifts += s
    return comparisons, shifts


def partitionD(arr, low, high):
    comparisons = 0
    shifts = 0
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    j = k = low + 1
    g, p, q = high - 1, arr[low], arr[high]

    while k <= g:
        if arr[k] < p:
            comparisons += 1
            shifts += 1
            arr[k], arr[j] = arr[j], arr[k]
            j += 1

        elif arr[k] >= q:
            comparisons += 3
            while arr[g] > q and k < g:
                g -= 1
            shifts += 1
            arr[k], arr[g] = arr[g], arr[k]
            g -= 1

            if arr[k] < p:
                shifts += 1
                arr[k], arr[j] = arr[j], arr[k]
                j += 1

        k += 1

    j -= 1
    g += 1

    arr[low], arr[j] = arr[j], arr[low]
    arr[high], arr[g] = arr[g], arr[high]
    shifts += 1
    shifts += 1

    return j, g, comparisons, shifts


def dualPivotQuickSort(arr, low, high, show=False):
    comparisons = 0
    shifts = 0
    if low < high:
        lp, rp, c, s = partitionD(arr, low, high)
        comparisons += c
        shifts += s
        if show:
            print(arr)

        c, s = dualPivotQuickSort(arr, low, lp - 1)
        comparisons += c
        shifts += s
        c, s = dualPivotQuickSort(arr, lp + 1, rp - 1)
        comparisons += c
        shifts += s
        c, s = dualPivotQuickSort(arr, rp + 1, high)
        comparisons += c
        shifts += s
    return comparisons, shifts


def select_qs(arr):
    return __select_qs(arr, 0, len(arr) - 1)


def __select_qs(arr, low, high):
    comparisons = 0
    shifts = 0
    comparisons += 1
    if low < high:
        mid = (low+high)//2
        _, c, s = select(arr, mid, low, high)
        comparisons += c
        shifts += s
        c, s = __select_qs(arr, low, mid - 1)
        comparisons += c
        shifts += s
        c, s = __select_qs(arr, mid + 1, high)
        comparisons += c
        shifts += s
    return comparisons, shifts


def select(arr, k, start, end):
    comparisons = 0
    shifts = 0
    comparisons += 1
    if start == end:
        return arr[start]
    pivot, c, s = partition(arr, start, end)
    comparisons += c
    shifts += s
    comparisons += 1
    if pivot == k:
        return arr[pivot], comparisons, shifts
    elif k < pivot:
        comparisons += 1
        return select(arr, k, start, pivot - 1), comparisons, shifts
    else:
        comparisons += 1
        return select(arr, k, pivot + 1, end), comparisons, shifts


def select_dqs(arr):
    return __select_dqs(arr, 0, len(arr) - 1)


def __select_dqs(arr, low, high):
    comparisons = 0
    shifts = 0
    comparisons += 1
    if low < high:
        mid1 = (low+high)//3
        mid2 = mid1*2
        _, c, s = select(arr, mid1, low, high)
        comparisons += c
        shifts += s
        _, c, s = select(arr, mid2, mid1, high)
        comparisons += c
        shifts += s
        c, s = __select_qs(arr, low, mid1 - 1)
        comparisons += c
        shifts += s
        c, s = __select_qs(arr, mid1 + 1, mid2 - 1)
        comparisons += c
        shifts += s
        c, s = __select_qs(arr, mid2 + 1, high)
        comparisons += c
        shifts += s
    return comparisons, shifts
