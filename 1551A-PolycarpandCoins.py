def polycarp(n):
    if n % 3 == 0:
        a1 = int(n / 3)
        a2 = int(n / 3)
        return [a1, a2]
    
    else:
        a1 = int(n / 3)
        a2 = int(n / 3) + 1
        if (a1 * 1) + (a2 * 2) > n:
            return [a2, a1]
        else:
            return [a1, a2]
            
t = int(input())
total_result = []

for i in range(t):
    n = int(input())
    total_result.append(polycarp(n))

for j in total_result:
    print(*j)