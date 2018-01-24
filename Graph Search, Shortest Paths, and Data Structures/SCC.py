import time
import sys

sys.setrecursionlimit(40000)

class vertex():
    def __init__(self, index):
        self.index = index
        self.color = 'white'
        self.discover_time = float('inf')
        self.find_time = float('inf')
    def add_color(self, co):
        self.color = co
    def add_discover_time(self, d):
        self.discover_time = d
    def add_find_time(self, f):
        self.find_time = f

def read_graph(path='SCC.txt'):
    file_txt = open(path)
    graph = {}
    graph_reverse = {}
    for line in file_txt.readlines():
        temp = line.split(' ')
        temp = temp[:-1]
        vertex_exa = int(temp[0])
        target_vertex = int(temp[1])
        if vertex not in graph.keys():
            graph[vertex_exa] = [target_vertex]
        else:
            graph[vertex_exa].append(target_vertex)
        if target_vertex not in graph_reverse.keys():
            graph_reverse[target_vertex] = [vertex_exa]
        else:
            graph_reverse[target_vertex].append(vertex_exa)

    for i in range(0, max(graph.keys()) + 1):
        if i not in graph.keys():
            graph[i] = []
        if i not in graph_reverse.keys():
            graph_reverse[i] = []
    return (graph, graph_reverse)

def dfs(graph, search_order = None):
    order = []
    vertices = {}
    components = []
    for u in range(0, max(graph.keys()) + 1):
        vertices[u + 1] = vertex(u + 1)
    time = 0
    if search_order == None:
        for u in graph.keys():
            if vertices[u].color == 'white':
                (time, order) = dfs_visit(graph, u, time, vertices, order)
        return (vertices, order)
    else:
        for u in search_order:
            if vertices[u].color == 'white':
                components.append(u)
                (time, order) = dfs_visit(graph, u, time, vertices, order)
        return (vertices, order, components)


def dfs_visit(graph, u, time, vertices, order):
    time = time + 1
    vertices[u].add_discover_time(time)
    vertices[u].add_color('gray')
    for v in graph[u]:
        if vertices[v].color == 'white':
            if time%200 == 0:
                print('recursing time: ', time)
            (time, order) = dfs_visit(graph, v, time, vertices, order)
    vertices[u].add_color('black')
    time = time + 1
    vertices[u].add_find_time(time)
    order.append(u)
    return (time, order)

def scc(graph, graph_reverse):
    (vertices, order) = dfs(test_graph_reverse)
    (vertices, order, components) = dfs(graph, order[::-1])
    return (vertices, components)

def main():
    print('<-------------loading data------------->')
    data_begin_time = time.time()
    # (graph, graph_reverse) = read_graph()
    test_graph = {1: [2], 2: [3, 5, 6],
                    3: [4, 7], 4: [3, 8], 5: [1, 6],
                    6: [7], 7: [6, 8], 8: [8]}
    test_graph_reverse = {1: [5], 2: [1],
                    3: [2, 4], 4: [3], 5: [2],
                    6: [2, 5, 7], 7: [3, 6], 8: [4, 7, 8]}
    data_end_time = time.time()
    print('<-------------data loaded: %f(s)------------->\n'%(data_end_time - data_begin_time))

    print('<-------------running dfs------------->')
    al_begin_time = time.time()
    (vertices, order) = dfs(test_graph_reverse)
    (vertices, components) = scc(test_graph, test_graph_reverse)
    al_end_time = time.time()
    print('<-------------dfs complete: %f(s) ------------->\n'%(al_end_time - al_begin_time))
    print(components)

if __name__ == '__main__':
    main()
