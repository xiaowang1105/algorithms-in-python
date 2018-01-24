import math
import operator

def read_data_stream(path='Median.txt'):
    data = []
    with open(path) as f:
        for item in f.readlines():
            data.append(int(item.strip('\n')))
    return data

class heap:
    """
    This is a data structure for heap
    The methods defines below: heap length, heap size, heapify, buildheap, extract, insert
    Attention: herein, input i is index directly used for python list (list[0] is the first element)
    """
    def __init__(self, list_A):
        self.list_A = list_A
    def heap_length(self): # heap max height
        if 2**(int(math.log2(self.length))) == self.length:
            return self.length
        else:
            return 2**(int(math.log2(self.length)) + 1)
    def heap_size(self):
        return len(self.list_A)
    def parent(self, i):
        return (int((i + 1)/2) - 1)
    def left(self, i):
        return (2*(i + 1) - 1)
    def right(self, i):
        return 2*(i + 1)
    def heapify(self, i, method):
        l, r = self.left(i), self.right(i)
        ops = {'max': (lambda x, y: x > y), \
                'min': (lambda x, y: x < y)}
        if l < self.heap_size() and ops[method](self.list_A[l], self.list_A[i]):
            temp = l
        else:
            temp = i
        if r < self.heap_size() and ops[method](self.list_A[r], self.list_A[temp]):
            temp = r
        if temp != i:
            self.list_A[i], self.list_A[temp]= self.list_A[temp], self.list_A[i]
            self.heapify(temp, method)
    def build_heap(self, method):
        size = self.heap_size()
        for i in range(int((size + 1)/2) - 1, -1, -1):
            self.heapify(i, method)
    def extremum(self):
        return self.list_A[0]
    def extract_extremum(self, method):
        if self.heap_size() < 1:
            raise ValueError("Heap doesnt't have any element right now")
        element = self.list_A[0]
        self.list_A[0] = self.list_A.pop()
        self.heapify(0, method)
        return element
    def insert(self, key, method):
        self.list_A.append(key)
        length = self.heap_size()
        i = length - 1
        ops = {'max': (lambda x, y: x < y), \
                'min': (lambda x, y: x > y)}
        while i > 0 and ops[method](self.list_A[self.parent(i)], self.list_A[i]):
            self.list_A[self.parent(i)], self.list_A[i] = \
             self.list_A[i], self.list_A[self.parent(i)]
            i = self.parent(i)

def median_maintenance(low_heap, high_heap, median, item):
    if low_heap.heap_size() == 0 and high_heap.heap_size() == 0:
        low_heap.insert(item, 'max')
        median.append(item)
    else:
        max_in_low = low_heap.extremum()
        if item > max_in_low:
            high_heap.insert(item, 'min')
        else:
            low_heap.insert(item, 'max')
        low_size, high_size = low_heap.heap_size(), high_heap.heap_size()
        while abs(low_size - high_size) >= 2:
            if low_size < high_size:
                temp = high_heap.extract_extremum('min')
                low_heap.insert(temp, 'max')
            else:
                temp = low_heap.extract_extremum('max')
                high_heap.insert(temp, 'min')
            low_size, high_size = low_heap.heap_size(), high_heap.heap_size()
        if low_size == high_size:
            median.append(low_heap.extremum())
        elif low_size > high_size:
            median.append(low_heap.extremum())
        else:
            median.append(high_heap.extremum())
        return median

def main():
    input_list = read_data_stream()
    low_heap = heap([])
    high_heap = heap([])
    median = []
    for item in input_list:
        median_maintenance(low_heap, high_heap, median, item)
    return median

if __name__ == '__main__':
    median = main()
    print(sum(median)%10000)
