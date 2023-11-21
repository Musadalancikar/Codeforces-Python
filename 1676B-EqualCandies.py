def min_eat_sugar(sugar_lst):
    min_sugar = min(sugar_lst)
    result = 0
    
    for j in range(n):
        result += (sugar_lst[j] - min_sugar)
        
    return result

t = int(input())
total = []

for i in range(t):
    n = int(input())
    sugar_lst = list(map(int, input().split()))
    total.append(min_eat_sugar(sugar_lst))
    
for k in total:
    print(k)
