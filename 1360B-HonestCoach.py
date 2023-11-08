def min_diff(lst):
    for j in range(len(lst)):
        x = lst.count(lst[j])
        if x > 1:
            return 0
    sort_list = sorted(lst)
    y = []
    for l in range(len(sort_list)-1):
        y.append(abs(sort_list[l] - sort_list[l+1]))
    
    return min(y)
    
t = int(input())
total = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    total.append(min_diff(lst))
    
for k in total:
    print(k)