def count_split_inv(left, right, length):
    mid = int(length/2)

    if not len(left) or not len(right): # Input arguments may be None type
        return left or right

    len_left = len(left)
    len_right = len(right)
    result = []
    i = 0
    j = 0
    count = 0
    while i < len_left and j < len_right:
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            count+= len_left - i
            # print(count)
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return (result, count)

def sort_and_count(array_A, length):
    if length == 1:
        return (array_A, 0)
    else:
        mid = int(length/2)
        (B, X) = sort_and_count(array_A[:mid], mid)
        (C, Y) = sort_and_count(array_A[mid:], length - mid)
        (D, Z) = count_split_inv(B, C, length)

    return (D, X + Y + Z)

def main():
    file_txt = open('IntegerArray.txt', 'r')
    data_list = [int(line.strip('\n')) for line in file_txt.readlines()]
    [sorted_list, number_inv] = sort_and_count(data_list, len(data_list))
    return number_inv

if __name__ == '__main__':
    # # test on small number
    # (result, count) = sort_and_count([10,2,3,22,33,7,4,1,2], 9)
    # print(count)

    # test on week assignment
    print('number of inversions is: ', main())
