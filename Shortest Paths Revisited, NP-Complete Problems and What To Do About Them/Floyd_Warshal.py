from tqdm import tqdm

def read_file(path='g1.txt'):
    with open(path) as f:
        (num_vertices, num_edges) = \
            list(map(int, f.readline().strip('\n').split(' ')))
        graph = {}
        for line in f.readlines():
            (head, tail, cost) = list(map(int, line.strip('\n').split(' ')))
            graph[(head, tail)] = cost
    return (num_vertices, num_edges, graph)

def floyd_warshal(num_vertices, num_edges, graph):
    bound = num_vertices + 1
    current_array = [[float('inf') for j in range(bound)] for i in range(bound)]
    last_array = current_array
    edges = set(graph.keys()) # important to set the data type to set
    for i in range(bound):
        for j in range(bound):
            if i == j:
                last_array[i][j] = 0
            elif (i, j) in edges:
                last_array[i][j] = graph[(i, j)]

    for k in range(1, bound):
        for i in range(1, bound):
            for j in range(1, bound):
                current_array[i][j] = \
                    min(last_array[i][j], last_array[i][k] + last_array[k][j])
                if i == j:
                    if current_array[i][j] < 0:
                        return "This graph has a negative cycle!"

    return min(min(current_array, key=lambda x: min(x)))

def main():
    for i in [1, 2, 3]:
        (num_vertices, num_edges, graph) = read_file(path='g'+str(i)+'.txt')
        cost = floyd_warshal(num_vertices, num_edges, graph)
        print('this is the result for graph' + str(i) + ' ', cost)

if __name__ == '__main__':
    main()
