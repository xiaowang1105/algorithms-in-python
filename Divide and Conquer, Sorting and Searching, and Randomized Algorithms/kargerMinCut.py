import random, copy, math, time

def read_graph(path='kargerMinCut.txt'):
    file_txt = open(path)
    graph = {}
    for line in file_txt.readlines():
        temp = line.split('\t')
        temp = temp[:-1]
        temp = list(map(int, temp))
        graph[temp[0]] = temp[1:]

    return graph

def random_choose(graph):
    u = random.choice(list(graph.keys()))
    v = random.choice(list(graph[u]))
    return u, v

def karger_min_cut(graph):
    while len(graph) > 2:
        u, v = random_choose(graph)
        graph[u].extend(graph[v]) # fuse the vertices
        for x in graph[v]: # delete all v, append all u
            graph[x].remove(v)
            graph[x].append(u)
        while u in graph[u]: # delete self loop
            graph[u].remove(u)
        del graph[v]

    for key in graph.keys():
        length = len(graph[key])
    return length

def run(n, graph):
    i = 0
    count = 1000000
    while i < n:
        data = copy.deepcopy(graph)
        min_cut = karger_min_cut(data)
        if min_cut < count:
            count = min_cut
        i = i + 1
    return count

if __name__ == '__main__':
    start_time = time.time()
    g = read_graph()
    length = len(g)
    n = 100
    print('min cut is: ', run(n, g))
    end_time = time.time()
    durings = end_time - start_time
    print('running %d times durings(s): %f' %(n, durings))
