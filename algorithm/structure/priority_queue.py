class MinHeap:
    def __init__(self, arr=None):
        self.arr = []
        for e in arr:
            self.push(e)

    def empty(self):
        return len(self.arr) == 0

    def heapify(self, idx):
        if self.empty():
            return
        n = len(self.arr)
        left = idx * 2 + 1
        right = idx * 2 + 2
        min_idx = idx
        if left < n and self.arr[left] < self.arr[min_idx]:
            min_idx = left
        if right < n and self.arr[right] < self.arr[min_idx]:
            min_idx = right
        if min_idx != idx:
            self.arr[idx], self.arr[min_idx] = self.arr[min_idx], self.arr[idx]
            self.heapify(min_idx)

    def extract_min(self):
        if self.empty():
            return None
        if len(self.arr) == 1:
            return self.arr.pop()
        min_v = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.heapify(0)
        return min_v

    def decrease_key(self, idx, v):
        self.arr[idx] = v
        self.sift_up(idx)

    def sift_up(self, idx):
        i = idx
        while i > 0 and self.arr[(i - 1) >> 1] > self.arr[i]:
            self.arr[i], self.arr[(i - 1) >> 1] = self.arr[(i - 1) >> 1], self.arr[i]
            i = (i - 1) >> 1

    def push(self, n):
        self.arr.insert(0, n)
        self.heapify(0)

    def pop(self):
        return self.extract_min()
