
n = int(input())

y = []
z = []

for i in range(n):
    m = list(map(int, input()))
    for i in range(len(m)):
        if m[i] > 0:
            x = m[i]*(10 ** (len(m)-(i+1)))
            y.append(x)
    z.append(y)
    y = []
    
for i in z:
    print(len(i))
    print(*i)