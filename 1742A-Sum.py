from itertools import combinations

n = int(input())

def comb(number_list):
    copy_number_list = number_list.copy()
    total = 0
    result = []
    combina_list = list(combinations(number_list, 2))
    for i in combina_list:
        for j in i:
            if j in copy_number_list:
                copy_number_list.remove(j)
        if sum(i) in copy_number_list:
            total += 1
            copy_number_list = number_list.copy()
        else:
            total = total
            copy_number_list = number_list.copy()
    
    if total >= 1:
        result.append("YES")
        total = 0
    else:
        result.append("NO")
        total = 0

    return result

total_result = []

for i in range(n):
    number_list = list(map(int, input().split()))
    total_result.append(comb(number_list))
    
for i in total_result:
    print(*i)

        

        


