def find_max_cross_subarray(A, low, mid, high):
    left_sum = float('-inf')
    temp_sum = 0
    for i in range(mid - 1, low - 1, -1):
    # tricy place in python, in python range(1,3) means only 1,2 without 3
        temp_sum = temp_sum + A[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i

    right_sum = float('-inf')
    temp_sum = 0
    for i in range(mid, high, 1):
        temp_sum = temp_sum + A[i]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = i
    return (max_left, max_right, left_sum + right_sum)


def find_max_subarray(A, low, high):
    # assert high >= low, 'high index smaller than low index error!'
    if low + 1 == high: # tricy place in python, in python A[low:high] doesn't include A[high]
        return (low, high, A[low])
    else:
        mid = int((low + high)/2)
        (left_low, left_high, left_sum) = find_max_subarray(A, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(A, mid, high)
        (cross_low, cross_high, cross_sum) = find_max_cross_subarray(A, low, mid, high)

    if (left_sum >= right_sum) and (left_sum >= cross_sum):
        return (left_low, left_high, left_sum)
    elif (right_sum >= left_sum) and (right_sum >= cross_sum):
        return (right_low, right_high, right_sum)
    else:
        return (cross_low, cross_high, cross_sum)

if __name__ == '__main__':
    A = [1,3,4,5,-1,23,-20,1,-10,3,-10,3]
    print(find_max_subarray(A, 0, len(A)))
