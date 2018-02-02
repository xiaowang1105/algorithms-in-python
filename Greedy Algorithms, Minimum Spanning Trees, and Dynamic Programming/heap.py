import math

class Vertex:
    def __init__(self, index, key):
        self.index = index
        self.key = key

class Heap:
    def __init__(self, queue):
        self.queue = queue
    def heap_size(self):
        return len(self.queue)

    def map_book(self):
        book = {}
        for i, v in enumerate(self.queue):
            book[v.index] = i
        return book

    @staticmethod
    def parent(i):
        return (int((i + 1)/2) - 1)
    @staticmethod
    def left(i):
        return (2*(i + 1) - 1)
    @staticmethod
    def right(i):
        return 2*(i + 1)

    def min_heapify(self, i):
        l, r = Heap.left(i), Heap.right(i)
        if l < self.heap_size() and self.queue[l].key < self.queue[i].key:
            temp = l
        else:
            temp = i
        if r < self.heap_size() and self.queue[l].key < self.queue[i].key:
            temp = r
        if temp != i:
            self.queue[i], self.queue[temp]= self.queue[temp], self.queue[i]
            self.min_heapify(temp)
    def build_min_heap(self):
        size = self.heap_size()
        for i in range(int((size + 1)/2) - 1, -1, -1):
            self.min_heapify(i)
    def extract_min(self):
        if self.heap_size() < 1:
            raise ValueError("Heap doesnt't have any element right now")
        element = self.queue[0]
        if self.heap_size() == 1:
            self.queue.pop()
        else:
            self.queue[0] = self.queue.pop()
            self.min_heapify(0)
        return element
    def insert(self, key):
        self.queue.append(key)
        length = self.heap_size()
        i = length - 1
        while i > 0 and self.queue[Heap.parent(i)].key > self.queue[i].key:
            self.queue[Heap.parent(i)], self.queue[i] = \
             self.queue[i], self.queue[Heap.parent(i)]
            i = Heap.parent(i)
    def decrease_key(self, i, key):
        if key < self.queue[i].key:
            self.queue[i].key = key
        while i > 0 and self.queue[Heap.parent(i)].key > self.queue[i].key:
            self.queue[Heap.parent(i)], self.queue[i] = \
             self.queue[i], self.queue[Heap.parent(i)]
            i = Heap.parent(i)

if __name__ == '__main__':
    q = [Vertex(1,1), Vertex(2,3), Vertex(3,5)]
    q = Heap(q)
    print(q.heap_size())
    print(q.extract_min().key)
    print(q.heap_size())
    print(q.queue)
