def medium_number(lst):
    lst.remove(min(lst))
    lst.remove(max(lst))
    return lst
    
t = int(input())
total_result = []
 
for i in range(t):
    lst = list(map(int, input().split()))
    total_result.append(medium_number(lst))
    
for j in total_result:
    print(*j)