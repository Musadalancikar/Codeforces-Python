def arithmetic(n, lst):
    if sum(lst) / n == 1.0:
        return 0
    else:
        if sum(lst) > n:
            return abs(n - sum(lst))
        else:
            return 1
            
t = int(input())
result = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    result.append(arithmetic(n, lst))
    
for j in result:
    print(j)