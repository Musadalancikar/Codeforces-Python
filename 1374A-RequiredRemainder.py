

t = int(input())

result = []
k = 0
for i in range(t):
    x, y, n = list(map(int, input().split()))
    k = int(n / x)
    if (y == 0) and (x > n) :
        result.append(0)
    else:
        if ((x*k) + y) <= n:
            result.append(((x*k) + y))
        else:
            result.append(((x*(k-1))+y))
            
for i in result:
    print(i)