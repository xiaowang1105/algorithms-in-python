import time
from tqdm import tqdm
from union_find import Union_Find

# in order to save memory, create a upper triangle matrix
## I don't want to use numpy :)
class Upper_tri:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.array = [0 for x in \
                        range(int((num_vertices)*(num_vertices - 1)/2))]
    def return_index(self, x, y):
        if x > y:
            return self.return_index(y, x)
        else:
            n = self.num_vertices - 1
            return int((((2 * n - x + 2) * (x - 1)) / 2 + y - x) - 1)
    def find(self, x, y):
        return self.array[self.return_index(x, y)]
    def change_value(self, x, y, value):
        self.array[self.return_index(x, y)] = value
    def return_position(self, x):
        n = self.num_vertices - 1
        i = 0
        while ((2 * n - i + 2) * (i - 1)) / 2 < x + 1:
            i += 1
        i -= 1
        j = int(x + i - ((2 * n - i + 2) * (i - 1)) / 2) + 1
        assert self.return_index(i, j) == x, 'return position error!'
        return (i, j)

def initialize(path='clustering1.txt'):
    with open(path) as f:
        num_vertices = int(f.readline().strip('\n'))
        matrix = Upper_tri(num_vertices)
        for item in f.readlines():
            temp = list(map(int, item.strip('\n').split(' ')))
            matrix.change_value(temp[0], temp[1], temp[2])
    vertices = [Union_Find() for x in range(num_vertices)]
    return (matrix, vertices)

def kruskal(matrix, vertices, stop_condition=1):
    num_vertices = len(vertices)
    list1 = matrix.array
    sort_index = sorted(range(len(list1)), key=lambda k: list1[k])
    T = []
    component = set([vertex for vertex in vertices])
    # print(len(component))
    # print('length of edges', len(sort_index))
    value = 0
    # for item in tqdm(sort_index):
    for item in sort_index:
        (i, j) = matrix.return_position(item)
        if vertices[i - 1].find_set() != vertices[j - 1].find_set():
            value += 1
            T.append(set([i, j]))
            if len(component) > stop_condition:
                delete = Union_Find.union(vertices[i - 1], vertices[j - 1])
                if delete in component:
                    component.remove(delete)
            elif len(component) == stop_condition:
                continue
            else:
                raise ValueError('component lenght error')
    # print('runnning times of if inside', value)
    flatten_T = sorted([i for item in T for i in list(item)])
    # print(len(list(set(flatten_T))), len(component))
    assert len(list(set(flatten_T))) == len(vertices) \
        and len(component) == stop_condition, 'Tree output error!'
    return (vertices, T, component, sort_index)

def clustering(matrix, vertices, num_class=4):
    (vertices, T, component, sort_index) = kruskal(matrix, vertices, num_class)
    component = list(component)
    num_component = len(component)
    distance_matrix = Upper_tri(num_component)
    defined_dis = []
    for item in sort_index:
        if len(defined_dis) == int(num_component * (num_component - 1) / 2):
            break
        (i, j) = matrix.return_position(item)
        vi_root, vj_root = vertices[i - 1].find_set(), vertices[j - 1].find_set()
        if vi_root != vj_root:
            index1, index2 = component.index(vi_root), component.index(vj_root)
            if set([index1, index2]) in defined_dis:
                continue
            distance_matrix.change_value(index1 + 1, index2 + 1, matrix.array[item])
            defined_dis.append(set([index1, index2]))
    return distance_matrix.array

def main():
    begin_time = time.time()
    (matrix, vertices) = initialize()
    print('loading data during(s): ', time.time() -  begin_time)
    begin_time = time.time()
    distance = clustering(matrix, vertices, num_class=4)
    print('four classes distance info is: ', distance)
    print('running algorithm during(s): ', time.time() - begin_time)

if __name__ == '__main__':
    main()
