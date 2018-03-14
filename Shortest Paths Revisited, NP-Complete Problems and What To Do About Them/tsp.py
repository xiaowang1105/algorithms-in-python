import math
import time
import itertools
import numpy
from tqdm import tqdm
from itertools import chain, combinations

def read_file(path='tsp.txt'):
    with open(path) as f:
        num_cities = int(f.readline().strip('\n'))
        graph = []
        for line in f.readlines():
            graph.append(tuple(map(float, line.strip('\n').split(' '))))
    return (num_cities, graph)

def computeSets(maxCardinality):
    """
    treat this function as a way of encoding
    Compute sets (combinations) of elements up to specified cardinality.
    Outputs a dictionary with keys specifying list of sets of a given
    cardinality.
    """
    sets = {}
    for num in range(maxCardinality + 1):
        sets[num] = []
    for num in range(2**maxCardinality):
        sets[bin(num).count('1')].append(num)
    return sets

def onesIndices(num):
    """Returns 0-based indices of set bits"""

    onesIndices = []
    bl = num.bit_length()
    for i in range(bl+1):
        if num & 0b1 == 1:
            onesIndices.append(i)
        num = num >> 1
    return onesIndices

def compute_distance(v1, v2):
    distance = math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)
    return distance

def tsp(num_cities, graph):
    """
    first of all, we should define a way to encode S, since list is not hashable
    herein, I choose a string to combine all the vertices
    """
    sets = computeSets(num_cities)
    A = np.ones((2**num_cities, num_cities), dtype='float')
    A = A * float('inf')
    # base case
    for i in range(2**num_cities):
        A[i, 0] = float('inf')
    A[1, 0] = 0
    for m in tqdm(range(2, num_cities + 1)):
        print("Computing subproblems of size ", m)
        for subset_index in sets[m]:
            if subset_index & 0b1 != 0b1:
                continue
            jCandidates = onesIndices(subset_index)

        xorMask = 2**j
        previousSet = subset_index ^ xorMask
        bestVal = float('inf')

        for k in jCandidates:
            if k == j:
                val = subproblemArr[2**len(points)-1, j] + distances[j, 0]
                shortestRoute = val if val < shortestRoute else shortestRoute

    return A, shortestRoute


def main():
    (num_cities, graph) = read_file()
    begin_time = time.time()
    (A, shortestRoute) = tsp(num_cities, graph)
    print('computing result during (s): ', time.time() - begin_time)

if __name__ == '__main__':
    main()
