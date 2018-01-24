def choose_pivot(array_A, pivot_selection):
    """
    This function is used to describe which way to choose pivot
    Arguments:
        array_A, an input list
        pivot_selection, a string
    Returns:
        pivot, the number of pivot
    """
    if pivot_selection == 'first':
        pivot = array_A[0]
    elif pivot_selection == 'final':
        pivot = array_A[-1]
    elif pivot_selection == 'median-of-three':
        first = array_A[0]
        final = array_A[-1]
        if len(array_A) % 2 == 0:
            middle = array_A[int(len(array_A)/2) - 1]
        else:
            middle = array_A[int(len(array_A)/2)]
        candidate = [first, final, middle]
        pivot = sum(candidate) - min(candidate) - max(candidate)
    else:
        print('pivot selection way doesn\'t exit')
        return None
    return pivot

def partition(array_A, pivot):
    index = array_A.index(pivot)
    # preprocess, putting the pivot in the first place
    array_A[0], array_A[index] = array_A[index], array_A[0]
    comparsion = 0
    i = 1
    for j in range(1, len(array_A)):
        comparsion = comparsion + 1
        if array_A[j] < pivot: # if the value smaller than pivot, moving before P
            array_A[i], array_A[j] = array_A[j], array_A[i]
            i = i + 1
    # swap pivot and (i-1)th element
    array_A[0], array_A[i - 1] = array_A[i - 1], array_A[0]

    return [array_A, comparsion]

def quick_sort(array_A, pivot_selection):
    """
    Besides sorting the array_A, this function also returns the total number \
    of comparsions (for the convenience of checking running time).
    Arguments:
        array_A, unsorted array_A
        pivot_selection, a string describing how to choose pivot
    Return:
        comparsion, number of comparsions in the process of sorting
    """
    length = len(array_A)
    if length <= 1:
        return 0
    pivot = choose_pivot(array_A, pivot_selection)
    (array_A, Z) = partition(array_A, pivot)
    # print('This time pivot is %d and after partition is :'%(pivot), array_A)
    index = array_A.index(pivot)
    left = array_A[:index]
    if index < length - 1:
        right = array_A[(index + 1):]
        X = quick_sort(left, pivot_selection)
        Y = quick_sort(right, pivot_selection)
        array_A[:index], array_A[index + 1:] = left, right
    else:
        X = quick_sort(left, pivot_selection)
        array_A[:index] = left
        Y = 0
    return (X + Y + Z)

def main():
    file_txt = open('QuickSort.txt')
    array_A = [int(line.strip('\n')) for line in file_txt.readlines()]
    comparsion = quick_sort(array_A, pivot_selection='median-of-three')
    return comparsion

if __name__ == '__main__':
    comparsion = main()
    print('number of comparsions is: ', comparsion)
