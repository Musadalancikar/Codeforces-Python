def min_mov(lst):
    return max(lst)-min(lst)
    
t = int(input())
total_result = []
 
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    total_result.append(min_mov(lst))
    
for j in total_result:
    print(j)