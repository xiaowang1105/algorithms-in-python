def insert_sort(array):
    length = len(array)
    for i in range(1, length):
        key = array[i]
        j = i - 1
        while j >= 0:
            if key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            else:
                break
        array[j + 1] = key

    return array

if __name__ == '__main__':
    result = insert_sort([1,4,2,19,8,3,12,5])
    print(result)
