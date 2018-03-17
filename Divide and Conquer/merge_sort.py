def merge(left, right):
    if not len(left) or not len(right): # Input arguments may be None type
        return left or right

    len_left = len(left)
    len_right = len(right)
    result = []
    i = 0
    j = 0
    while (len(result) < len_left + len_right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        if i == len_left or j == len_right:
            result.extend(left[i:] or right[j:])
            break
    return result

def merge_sort(input_list):
    if len(input_list) < 2:
        return input_list
    else:
        mid = int(len(input_list)/2)
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])

    return merge(left, right)

if __name__ == '__main__':
    result = merge_sort([1,3,2,19,1,3,12,4])
    print(result)
