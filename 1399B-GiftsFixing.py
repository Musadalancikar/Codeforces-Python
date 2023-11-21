def min_fixing(a,b):
    x = min(a)
    y = min(b)
    total = 0
    while True:
        for j in range(len(a)):
            if a[j] > x and b[j] > y:
                new_a = a[j]
                total += min((a[j] - x),(b[j] - y))
                a[j] -= min((a[j] - x),(b[j] - y))
                b[j] -= min((new_a - x),(b[j] - y))
            elif a[j] > x and b[j] <= y:
                total += (a[j] - x)
                a[j] = x
            elif a[j] <= x and b[j] > y:
                total += (b[j] - y)
                b[j] = y
            elif max(a) == x and max(b) == y:
                return total
                break

t = int(input())
total_result = []

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total_result.append(min_fixing(a, b))

for k in total_result:
    print(k)    
    
