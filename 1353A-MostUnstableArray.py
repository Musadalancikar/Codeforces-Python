def unstable_array(n,m):
    if n == 1:
        return 0
    elif n == 2:
        return m
    else:
        return m*2


t = int(input())
total = []

for i in range(t):
    n, m = map(int, input().split())
    total.append(unstable_array(n, m))
    
for k in total:
    print(k)