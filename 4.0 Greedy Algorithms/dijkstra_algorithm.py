def read_graph(path = 'dijkstraData.txt'):
    f = open(path)
    graph = {}
    for line in f.readlines():
        temp = line.split('\t')
        temp = temp[:-1]
        temp = [list(map(int, item.split(','))) for item in temp]
        graph[temp[0][0]] = temp[1:]
    return graph

def update_dist(graph, explored_vertex, dist):
    for v in explored_vertex:
        connect_to_v = [i[0] for i in graph[v]]
        difference_set = list(set(explored_vertex)^set(list(graph.keys())))
        for w in difference_set:
            if w in connect_to_v:
                if dist[w] > dist[v] + graph[v][connect_to_v.index(w)][1]:
                    dist[w] = dist[v] + graph[v][connect_to_v.index(w)][1]
    return dist

def dijkstra(graph, source):
    dist = {}
    dist[source] = 0
    explored_vertex = [source]
    connect_to_v = [i[0] for i in graph[source]]
    difference_set = list(set(explored_vertex)^set(list(graph.keys())))
    for w in difference_set:
        if w in connect_to_v:
            dist[w] = dist[source] + graph[source][connect_to_v.index(w)][1]
        else:
            dist[w] = float('inf')
    i = 0
    while difference_set != []:
        if i%100 == 0:
            print('during %d iterations'%i)
            print('current explored_vertex is: ', explored_vertex)
            print('current difference_set is:', difference_set)
        difference_set = list(set(explored_vertex)^set(list(graph.keys())))
        min_dist = float('inf')
        min_index = 0
        for item in difference_set:
            if dist[item] < min_dist:
                min_dist, take_in_vertex = dist[item], item
        explored_vertex.append(take_in_vertex)
        dist = update_dist(graph, explored_vertex, dist)
        i = i + 1
    return dist

if __name__ == '__main__':
    test_graph = {1: [(2, 2), (3, 3)], 2: [(1, 2), (3, 2), (4, 1)],
             3: [(1, 1), (2, 2), (4, 1)], 4: [(2, 1), (3, 1), (5, 2)],
             5: [(4, 2)]}
    graph = read_graph()
    print(graph.keys())
    print('running dijkstra...')
    dist = dijkstra(graph, 1)
    [print(dist[i]) for i in [7,37,59,82,99,115,133,165,188,197]]
