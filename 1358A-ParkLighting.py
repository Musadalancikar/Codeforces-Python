def lighing(n, m):
    if n * m == 1:
        return 1
    elif n * m % 2 == 1:
        return int((n*m)/2) + 1
    else:
        return int((n*m)/2)
    
t = int(input())
total = []

for i in range(t):
    n, m = map(int, input().split())
    total.append(lighing(n, m))
    
for j in total:
    print(j)