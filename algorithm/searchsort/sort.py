import random


def selection_sort(arr):
    """
    find the smallest ele in the array from zero to last one by one, and put the smallest ele at the last of ordered array
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


def bubble_sort(arr):
    """
    Bubble sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
    if they are in wrong order.
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def insertion_sort(arr):
    """
    Insertiong sort is a simple sorting algorithm that works the way we sort playing cards in our hands
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    """
    It divides the input array in two halves, call itself for the two halves and then merges the two sorted halves
    :param arr:
    :return:
    """
    if len(arr) > 1:
        m = len(arr) >> 1
        L, R = arr[:m], arr[m:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = R[j]
                j += 1
            else:
                arr[k] = L[i]
                i += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def heap_sort(arr):
    """
    build a maximum heap, swap the first ele to the end, loop from n-i to 0
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)


def quick_sort(arr, l, r):
    """
    select a ele as pivot, place the ele which is less than pivot to the left, place the ele which is great then pivot
    to the right, recur do the left partition and right partition
    :param arr:
    :param l:
    :param r:
    :return:
    """
    if l < r:
        pi = _partition(arr, l, r)
        quick_sort(arr, l, pi - 1)
        quick_sort(arr, pi + 1, r)


def radix_sort(arr):
    """
    从低位到高位依次比较排序元素，最终保证数据有序
    :param arr:
    :return:
    """
    exp = 1
    m = max(arr)
    while m // exp > 0:
        _counting(arr, exp)
        exp *= 10


def counting_sort(arr):
    """
    计数排序
    :param arr:
    :return:
    """
    n = len(arr)
    output = [0] * 256
    count = [0] * 256
    ans = [''] * n
    for i in arr:
        count[ord(i)] += 1
    for i in range(1, 256):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1
        i -= 1
    for i in range(n):
        ans[i] = output[i]
    return ''.join(ans)


def shell_sort(arr):
    """
    Shell sorting is a sorting algorithm that like insertion sort but has gabs, initial gab is n/2, shrink the gap to 1
    :param arr:
    :return:
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j] < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            if j != i:
                arr[j] = temp


def comb_sort(arr):
    """
    Comb sort like bubble sort but swap gap internal
    :param arr:
    :return:
    """
    n = len(arr)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        swapped = False
        gap = _next_gap(gap)
        print(gap)
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                swapped = True
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
        if gap == 1:
            swapped = False


def pigeonhole_sort(arr):
    """
    Pigeonhole sorting is a sorting algorithm that is suitable for sorting lists of elements where the number of elements
    and the number of possible key values are approximately the same
    :param arr:
    :return:
    """
    n = len(arr)
    max_v = max(arr)
    min_v = min(arr)
    holes = [0] * (max_v - min_v + 1)
    for i in range(n):
        holes[arr[i] - min_v] += 1
    i = 0
    for j in range(len(holes)):
        while holes[j] > 0:
            arr[i] = min_v + j
            holes[j] -= 1
            i += 1


def cycle_sort(arr):
    """
    The idea of cycle sort is that array to be sorted can be divided into cycles, Start cycle from 0 to n-1,
    Find the correct place of current item
    then replace it, repeatedly find the old value's correct place till the pos equals to the cycle start
    :param arr:
    :return:
    """
    n = len(arr)
    writes = 0
    for cycle_start in range(0, n - 1):
        pos = cycle_start
        item = arr[cycle_start]
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
        # if no cycle, continue next cycle
        if pos == cycle_start:
            continue
        # put the item there or right after the duplicates
        while arr[pos] == item:
            pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            while arr[pos] == item:
                pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1
    print(writes)


def _next_gap(gap):
    gap = (gap * 10) // 13
    if gap <= 1:
        return 1
    return gap


def _counting(arr, exp):
    """
    计数排序
    :param arr:
    :param exp:
    :return:
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]


def _partition(arr, l, r):
    """
    快排分区选取pivot
    :param arr:
    :param l:
    :param r:
    :return:
    """
    r_idx = random.randint(l, r)
    pivot = arr[r_idx]
    arr[r_idx], arr[r] = arr[r], arr[r_idx]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = pivot, arr[i + 1]
    return i + 1


def _heapify(arr, n, i):
    """
    在指定位置堆化arr
    :param arr:
    :param n:
    :param i:
    :return:
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        _heapify(arr, n, largest)


if __name__ == '__main__':
    arr = [9, 2, 18, 8, -3, 2, 32, 21, 16, 6, -9, -8, 22, 20]
    arr = [4, 3, 5, 2, 1, 3, 2, 3]
    print(arr)
    # arr = list(range(-5, 10, 2))
    # selection_sort(arr)
    # bubble_sort(arr)
    # insertion_sort(arr)
    # merge_sort(arr)
    # heap_sort(arr)
    quick_sort(arr, 0, len(arr) - 1)
    # radix_sort(arr)
    # comb_sort(arr)
    # pigeonhole_sort(arr)
    # cycle_sort(arr)
    print(arr)
    # cstr = 'qwerety5uiopas1dfghjklz4xcvbnm'
    # print(counting_sort(cstr))
