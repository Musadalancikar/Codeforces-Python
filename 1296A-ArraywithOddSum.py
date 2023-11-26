def array_odd_sum(lst):
    if sum(lst) % 2 == 1:
        return "YES"
    else:
        odd_lst = []
        even_lst = []
        for j in lst:
            if j % 2 == 1:
                odd_lst.append(j)
            else:
                even_lst.append(j)
        if len(odd_lst) % 2 == 1 or len(odd_lst) == 0 or len(even_lst) == 0:
            return "NO"
        else:
            return "YES"


t = int(input())
total = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    total.append(array_odd_sum(lst))
    
for k in total:
    print(k)