def fair_playof(lst):
    lst1 = lst[:2]
    lst2 = lst[2:]
    
    max_lst1 = max(lst1)
    max_lst2 = max(lst2)
    
    lst.remove(max_lst1)
    lst.remove(max_lst2)
    
    if max(lst) > max_lst1 or max(lst) > max_lst2:
        return "NO"
    else:
        return  "YES"

t = int(input())
total = []

for i in range(t):
    lst = list(map(int, input().split()))
    total.append(fair_playof(lst))
    
for j in total:
    print(j)