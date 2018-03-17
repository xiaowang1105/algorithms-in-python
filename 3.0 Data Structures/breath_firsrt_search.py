graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6], 3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }
def bfs(graph, start):
    path = []
    queue = [start]
    while(queue):
        vertex = queue.pop(0)
        if vertex not in path:
            path.append(vertex)
            queue.extend(graph[vertex])

    return path

print(bfs(graph, 0))
