def find_unsort_arr(arr):
    """
    1.Scan left to right find the first element which is greater then next element, let be s
    2.Scan right to left find the first element which is smaller than next element, let be e
    3.Check whether sorting the candidate unsorted sub array [s, e] makes the complete array sorted or not, if not, then
    include more elements in the subarray
    find the min, max of sub array[s, e], find the first element of arr[0,s-1] which is greater than min, change s to
    index of this element, find the first element of arr[e+1, n-1] which is smaller than max, change e to index of this
    element
    :param arr:
    :return:
    """
    n = len(arr)
    start, end = 0, n-1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            start = i
            break
    if start == 0:
        print("The complete array is sorted")
        exit()
    for i in range(n-1, 1, -1):
        if arr[i] < arr[i-1]:
            end = i
            break
    sub_arr = arr[start:end+1]
    min_v, max_v = min(sub_arr), max(sub_arr)
    for i in range(start-1, 0, -1):
        if arr[i] > min_v:
            start = i
            break
    for i in range(end+1, n):
        if arr[i] < max_v:
            end = i
            break
    return start, end


if __name__ == '__main__':
    arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    # arr = [1,2,3,4,5,6,7,8,9]
    print(find_unsort_arr(arr))