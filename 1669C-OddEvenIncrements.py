def odd_and_even(n, lst):
    odd = 0
    even = 0
    for j in range(n):
        if j % 2 == 0:
            if lst[j] % 2 == 0:
                even += 1
            else:
                odd += 1
    if even >= 1 and odd >= 1:
        return "NO"
    
    odd1 = 0
    even1 = 0
    for j in range(n):
        if j % 2 == 1:
            if lst[j] % 2 == 0:
                even1 += 1
            else:
                odd1 += 1
    if even1 >= 1 and odd1 >= 1:
        return "NO"
    
    else:
        return "YES"
    
t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    print(odd_and_even(n, lst))
    