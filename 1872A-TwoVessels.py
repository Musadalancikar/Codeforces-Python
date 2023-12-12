def velles(a, b, c):
    d = abs(a - b)
    return (d + (2 * c) - 1) // (2 * c)


t = int(input())
result = []

for i in range(t):
    a, b, c = map(int, input().split())
    result.append(velles(a, b, c)) 
    
for k in result:
    print(k)