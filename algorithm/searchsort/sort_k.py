from heapq import heapify, heappop, heappush


# sort a nearly sorted(k sorted) array,
# 1.Create a min heap of size k+1 with first k+1 elements
# 2.One by one remove min ele from heap, put it in result array, and add a new element to heap from remaining elements

def sort_k(arr, k):
    n = len(arr)
    # taken first kth ele
    heap = arr[:k+1]
    heapify(heap)
    target_idx = 0
    for rem_idx in range(k+1, n):
        arr[target_idx] = heappop(heap)
        heappush(heap, arr[rem_idx])
        target_idx += 1
    while heap:
        arr[target_idx] = heappop(heap)
        target_idx += 1


if __name__ == '__main__':
    arr = [2, 6, 3, 12, 56, 8]
    sort_k(arr, 3)
    print(arr)
