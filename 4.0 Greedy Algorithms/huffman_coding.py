import math

class Vertex:
    def __init__(self, index, key, leftChild=None, rightChild=None):
        self.index = index
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild

class Heap:
    def __init__(self, queue):
        self.queue = list(queue)
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
        if r < self.heap_size() and self.queue[r].key < self.queue[temp].key:
            temp = r
        if temp != i:
            self.queue[i], self.queue[temp] = self.queue[temp], self.queue[i]
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

def read_file(path='huffman.txt'):
    with open(path) as f:
        number_of_symbols = int(f.readline().strip('\n'))
        symbol_weight = {}
        for index in range(number_of_symbols):
            symbol_weight[index] = int(f.readline().strip('\n'))
    return symbol_weight

def huffman_coding(symbol_weight):
    depth_store = {}
    symbol_list = list(symbol_weight.keys())
    n = len(symbol_list)
    queue = [Vertex(index, value) for index, value in symbol_weight.items()]
    tree_nodes = list(queue)
    heap = Heap(queue)
    heap.build_min_heap()
    for i in range(n - 1):
        x_v = heap.extract_min()
        y_v = heap.extract_min()
        z_v = Vertex(n + i, x_v.key+y_v.key)
        z_v.leftChild = tree_nodes[x_v.index]
        z_v.rightChild = tree_nodes[y_v.index]
        heap.insert(z_v)
        tree_nodes.append(z_v)
    return queue, tree_nodes

def map_book(queue, tree_nodes):
    n = len(queue)
    tree_root = tree_nodes[-1]
    symbol2bits, bits2symbol = {}, {}
    def traverse(node, bits):
        if node.index <= n - 1:
            symbol2bits[node.index] = bits
            bits2symbol[bits] = node.index
        else:
            traverse(node.leftChild, bits + '0')
            traverse(node.rightChild, bits + '1')

    traverse(tree_root, '')

    return symbol2bits, bits2symbol

def main():
    symbol_weight = read_file()
    queue, tree_nodes = huffman_coding(symbol_weight)
    symbol2bits, bits2symbol = map_book(queue, tree_nodes)
    word_len_rank = sorted(symbol2bits, key=lambda x: len(symbol2bits[x]))
    print('the shortest word length is: ', len(symbol2bits[word_len_rank[0]]))
    print('the longest word length is: ', len(symbol2bits[word_len_rank[-1]]))

if __name__ == '__main__':
    main()
