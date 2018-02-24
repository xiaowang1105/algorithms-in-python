import time
from tqdm import tqdm

def read_file(path='knapsack_big.txt'):
    with open(path) as f:
        items = []
        knapsack_size, num_items = \
            list(map(int, f.readline().strip('\n').split(' ')))
        for line in f.readlines():
            items.append(list(map(int, line.strip('\n').split(' '))))
    return knapsack_size, num_items, items

def knapsack_bottom_up(knapsack_size, num_items, items):
    A = [0 for j in range(knapsack_size + 1)]
    for x in range(knapsack_size + 1):
        A[x] = 0
    for i in tqdm(range(1, num_items + 1)): # from 0 to num_items - 1
        for x in range(knapsack_size + 1): # from 0 to W + 1
            temp_value, temp_weight = items[i - 1][0], items[i - 1][1]
            if x >= temp_weight:
                A[x] = max(A[x], A[x - temp_weight] + temp_value)
    return A

def main():
    begin_time = time.time()
    knapsack_size, num_items, items = read_file()
    A = knapsack_bottom_up(knapsack_size, num_items, items)
    print('optimal value for knapsack problem is: ', A[knapsack_size])
    print('computation during (s): ', time.time() - begin_time)

if __name__ == '__main__':
    main()
