def new_programing(a, b, n):
    total = 0
    while True:
        if a > n:
            return total
            break
        else:
            if a > b:
                a += b
                b = (a - b)
                total += 1
            else:
                a += b
                total += 1
                
t = int(input())
result = []

for i in range(t):
    a, b, n = map(int, input().split())
    result.append(new_programing(a, b, n))
    
for j in result:
    print(j)