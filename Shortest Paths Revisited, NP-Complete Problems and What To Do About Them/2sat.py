import random
from math import log
from tqdm import tqdm

def read_file(path='2sat1.txt'):
    with open(path) as f:
        num_clauses = int(f.readline().strip('\n'))
        clauses = []
        for line in f.readlines():
            clauses.append(list(map(int, line.strip('\n').split(' '))))

    return num_clauses, clauses

def is_positive(number):
    if(number>0):
        return True
    else:
        return False

def is_sat(clauses_dict, clauses):
    for item in clauses:
        first_clause = clauses_dict[item[0] - 1] if is_positive(item[0]) \
                        else 1-clauses_dict[(abs(item[0]) - 1)]
        second_clause = clauses_dict[item[1] - 1] if is_positive(item[1]) \
                        else 1-clauses_dict[(abs(item[1]) - 1)]
        result =  first_clause and second_clause

        if(not result):
            return False

def initialize(num_clauses):
    clauses_dict = []
    for i in range(num_clauses):
        clauses_dict.append(random.randint(0, 1))

    return clauses_dict

def Papadimitriou(num_clauses, clauses):
    success_flag = 0
    for i in range(int(log(num_clauses, 2))):
        print("Running %d times"%i)
        clauses_dict = initialize(num_clauses)
        if(success_flag == 1):
            break
        for j in tqdm(range(2*num_clauses**2)):
            # if(j%1000000==0):
            #     print("\tInner loop %d times"%j)
            if(is_sat(clauses_dict, clauses)):
                success_flag = 1
                break
            else:
                temp = random.randint(0, num_clauses-1)
                clauses_dict[temp] = int(not clauses_dict[temp])

    return success_flag

def main():
    num_clauses, clauses = read_file()
    success_flag = Papadimitriou(num_clauses, clauses)
    print(success_flag) # 101100

if __name__ == '__main__':
    main()
