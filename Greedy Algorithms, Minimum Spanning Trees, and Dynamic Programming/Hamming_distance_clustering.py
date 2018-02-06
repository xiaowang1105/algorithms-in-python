import time
from tqdm import tqdm
from union_find import Union_Find

def initialize(path='clustering_big.txt'):
    vertices = {}
    with open(path) as f:
        num_vertices, num_bit = list(map(int, f.readline().strip('\n').split(' ')))
        for item in f.readlines():
            # it is crucial to read line as a hashable data type
            temp = ''.join(item.strip('\n').split(' '))
            # it doesn't matter if we treat two identical node as one
            vertices[temp] = Union_Find()
    return vertices

def two_bit_flip(node):
    """Give all the nodes by flipping one or two bits of the binary number
    representation of a node."""

    node_list = list(node)
    out = set()
    bit_length = len(node_list)
    for i in range(bit_length):
        for j in range(bit_length):
            new_node = node_list[:]
            if i != j:
                new_node[i] = ('1' if node[i] == '0' else '0')
                new_node[j] = ('1' if node[j] == '0' else '0')
            else:
                new_node[i] = ('1' if node[i] == '0' else '0')
            out.add(''.join(new_node))
    return out

def hamming_distance_clustering(vertices):
    num_vertices = len(vertices)
    # component = set([vertex for vertex in vertices.values()])
    num_component = len(vertices.values())
    value = 0
    all_vertices = vertices.keys()
    for vertex1 in tqdm(all_vertices):
        flip_out = two_bit_flip(vertex1)
        actual_vertices = flip_out.intersection(all_vertices)
        for vertex2 in actual_vertices:
            if vertices[vertex2].find_set() != vertices[vertex1].find_set():
                value += 1
                delete = Union_Find.union(vertices[vertex1], vertices[vertex2])
                num_component -= 1
    return num_component

def main():
    begin_time = time.time()
    vertices = initialize()
    print('loading data during(s): ', time.time() - begin_time)
    begin_time = time.time()
    num_component = hamming_distance_clustering(vertices)
    print('at least %d classes'%num_component)
    print('runing algorithm during(s): ', time.time() - begin_time)

if __name__ == '__main__':
    main()
