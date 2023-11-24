def count_greater(t, lst):
    total = 1
    total_lst = []
    for i in range(t-1):
        if lst[i] < lst[i+1]:
            total += 1
        else:
            total_lst.append(total)
            total = 1
    total_lst.append(total)
            
    return max(total_lst)

t = int(input())
lst = list(map(int, input().split())) 

print(count_greater(t, lst))   