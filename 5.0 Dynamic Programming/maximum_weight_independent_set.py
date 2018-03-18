def read_file(path='mwis.txt'):
    with open(path) as f:
        number_of_tasks = int(f.readline().strip('\n'))
        weight_list = []
        for index in range(number_of_tasks):
            weight_list.append(int(f.readline().strip('\n')))
    return weight_list

def wis(weight_list):
    n = len(weight_list)
    A = [0 for i in range(n + 1)]
    A[1] = weight_list[0]
    for i in range(2, n + 1):
        A[i] = max(A[i - 1], A[i - 2] + weight_list[i - 1])
    return A

def reconstruction(A, weight_list):
    S = {}
    for i in range(len(weight_list)):
        S[i] = 0
    i = len(weight_list)
    while i >= 2:
        if A[i - 1] > A[i - 2] + weight_list[i - 1]:
            i -= 1
        else:
            S[i - 1] = 1
            i -= 2
    S[0] = 1
    return S

def main():
    weight_list = read_file()
    A = wis(weight_list)
    print(A[-1])
    S = reconstruction(A, weight_list)
    check_set = [1, 2, 3, 4, 17, 117, 517, 997]
    check_set = [i - 1 for i in check_set]
    bool_value = [S[i] for i in check_set]
    bool_value = list(map(str, bool_value))
    bool_value = ''.join(bool_value)
    print(bool_value)

if __name__ == '__main__':
    main()
