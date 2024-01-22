n, m = map(int, input().split())

x = 0
a = 0
for i in range(n+1):
    b = n - a**2
    if a + b**2 == m and b >= 0:
        x += 1
        a += 1
    else:
        a += 1

print(x)
        
    