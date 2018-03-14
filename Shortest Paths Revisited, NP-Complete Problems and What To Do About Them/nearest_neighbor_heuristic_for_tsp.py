import numpy as np
from tqdm import tqdm
from math import sqrt

def read_file(path='nn.txt'):
    with open(path) as f:
        num_cities = int(f.readline().strip('\n'))
        graph = {}
        for line in f.readlines():
            temp_list = list(map(float, line.strip('\n').split(' ')))
            graph[int(temp_list[0])] = (temp_list[1], temp_list[2])

        return num_cities, graph

def euc_dist(x, y):
    distance = sqrt(pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2))
    return distance

def comp_shortest_dist_from_one_city(source_city, destination_cites, graph):
    dist_array = []
    for city in destination_cites:
        dist_array.append([city, euc_dist(graph[source_city], graph[city])])
    dist_array = sorted(dist_array, key=lambda x: (x[1], x[0]))

    return dist_array[0]

def find_next_city(start_city, graph, visited_cites, cities_set, tour_length):
    destination_cites = cities_set - visited_cites
    (next_city, s_dist) = \
            comp_shortest_dist_from_one_city(start_city, destination_cites, graph)
    visited_cites.add(next_city)
    tour_length += s_dist

    return  next_city, visited_cites, tour_length


def nn_tsp(num_cities, graph):
    visited_cites = set([1])
    cities_set = set([i for i in range(1, num_cities + 1)])
    tour_length = 0
    next_city, visited_cites, tour_length = \
        find_next_city(1, graph, visited_cites, cities_set, tour_length)
    while len(visited_cites) != num_cities:
        if (len(visited_cites) -1) % 100 == 0:
            print('Have processed %d cities'%len(visited_cites))
        next_city, visited_cites, tour_length = \
            find_next_city(next_city, graph, visited_cites, cities_set, tour_length)
    last_hop = euc_dist(graph[next_city], graph[1])
    tour_length += last_hop

    return tour_length



def main():
    num_cities, graph = read_file()
    tour_length = nn_tsp(num_cities, graph)
    print(tour_length)

if __name__ == '__main__':
    main()
