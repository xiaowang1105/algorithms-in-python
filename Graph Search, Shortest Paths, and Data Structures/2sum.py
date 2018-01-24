import bisect
from time import time

def read_data(path='2sum.txt'):
    array = []
    with open(path) as f:
        for item in f.readlines():
            array.append(item)
    array.sort()
    return array
def find_2sum(array):
    RANGE = 10000
    out = set()
    for item in array:
        lower = bisect.bisect_left(array, -WIDTH - i)
        upper = bisect.bisect_right(array, WIDTH - i)
        out |= set([i + j for j in array[lower:upper]])
    return out

def main():
    array = read_data()
    out =  find_2sum(array)
    return len(out)

if __name__  == '__main__':
    print(main())
