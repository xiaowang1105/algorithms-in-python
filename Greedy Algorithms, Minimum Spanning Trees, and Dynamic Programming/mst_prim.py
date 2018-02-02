# Results:
#     total running time for naive implement of prim alg is 3.498716 (s)
#     total running time for heap based implement of prim alg is 1.859750 (s)
import time
from heap import Vertex, Heap

def read_from_txt(path='edges.txt'):
    with open(path) as f:
        num_nodes, num_edges = \
            list(map(int, f.readline().strip('\n').split(' ')))
        weighted_graph = {}
        for i in range(1, num_nodes + 1):
            weighted_graph[i] = {}
        for line in f.readlines():
            v1, v2, cost = list(map(int, line.strip('\n').split(' ')))
            weighted_graph[v1][v2] = cost
            weighted_graph[v2][v1] = cost # this is an undirected graph
    return (num_nodes, num_edges, weighted_graph)

# naive implementaion of prim algorithm
def naive_mst_prim(weighted_graph):
    V = list(weighted_graph.keys())
    X = [1]
    T = []
    total_cost = 0
    while set(X) != set(V):
        min_dist = float('inf')
        for v1 in X:
            for v2 in weighted_graph[v1].keys():
                if v2 not in X:
                    if weighted_graph[v1][v2] < min_dist:
                        min_dist, temp_v2, temp_v1 = weighted_graph[v1][v2], v2, v1
        total_cost += min_dist
        T.append(set([temp_v1, temp_v2]))
        X.append(temp_v2)
    return total_cost

# heap based implementation of prim algorithm
def update_queue(X, V, weighted_graph, q):
    book = q.map_book()
    q = Heap([])
    for x in (set(V) - set(X)):
        if set(weighted_graph[x].keys()) & set(X) == set():
            q.insert(Vertex(x, float('inf')))
        else:
            key = min([weighted_graph[x][item] \
                for item in set(weighted_graph[x].keys()) & set(X)])
            q.insert(Vertex(x, key))
    return q

def heap_mst_prim(weighted_graph):
    V = list(weighted_graph.keys())
    X = [1]
    total_cost = 0
    q = Heap([])
    # initialize
    q = update_queue(X, V, weighted_graph, q)
    while set(X) != set(V):
        size = q.heap_size()
        element = q.extract_min()
        new_size = q.heap_size()
        assert new_size + 1 == size, 'wrong implement of heap'
        total_cost += element.key
        X.append(element.index)
        q = update_queue(X, V, weighted_graph, q)
    return total_cost

def main():
    weighted_graph = read_from_txt()[2]
    begin_time = time.time()
    cost1 = naive_mst_prim(weighted_graph)
    end_time = time.time()
    print('total time for naive implement of prim alg is %f'%(end_time - begin_time))
    begin_time = time.time()
    cost2 = heap_mst_prim(weighted_graph)
    end_time = time.time()
    print('total time for heap based implement of prim alg is %f'%(end_time - begin_time))
    assert cost1 == cost2, 'two implementation different'

if __name__ == '__main__':
    main()
