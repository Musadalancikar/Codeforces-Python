def color_even(lst):
    even_list = []
    odd_list = []
    for j in lst:
        if j % 2 == 0:
            even_list.append(j)
        else:
            odd_list.append(j)
    
    if len(odd_list) % 2 == 1:
        return "NO"
    else:
        return "YES"

t = int(input())
total = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    total.append(color_even(lst))
    
for k in total:
    print(k)
