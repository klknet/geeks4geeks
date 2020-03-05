class MaxHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, d):
        self.heap.append(d)
        self._siftdown(0, self.size() - 1)

    def pop(self):
        latest = self.heap.pop()
        if self.heap:
            ele = self.heap[0]
            self.heap[0] = latest
            self._siftup(0)
            return ele
        return latest

    def top(self):
        return self.heap[0]

    def _siftdown(self, start, pos):
        new_item = self.heap[pos]
        while pos > start:
            parent = (pos - 1) >> 1
            if new_item > self.heap[parent]:
                self.heap[pos] = self.heap[parent]
                pos = parent
                continue
            break
        self.heap[pos] = new_item

    def _siftup(self, pos):
        new_item = self.heap[0]
        startPos = pos
        end = self.size()
        child = 2 * pos + 1
        while child < end:
            right = child + 1
            if right < end and self.heap[right] > self.heap[child]:
                child = right
            self.heap[pos] = self.heap[child]
            pos = child
            child = 2 * pos + 1
        self.heap[pos] = new_item
        self._siftdown(startPos, pos)

    def empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


if __name__ == "__main__":
    h = MaxHeap()
    h.push(5)
    h.push(2)
    h.push(8)
    h.push(10)
    h.push(1)
    while not h.empty():
        print(h.pop())
