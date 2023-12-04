def grab_the_candies(n, lst):
    mihia_lst = []
    bianca_lst = []
    for j in range(n):
        if lst[j] % 2 == 0:
            mihia_lst.append(lst[j])
        else:
            bianca_lst.append(lst[j])
            
    if sum(mihia_lst) > sum(bianca_lst):
        return "YES"
    else:
        return "NO"

t = int(input())
total = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    total.append(grab_the_candies(n, lst))

for k in total:
    print(k)