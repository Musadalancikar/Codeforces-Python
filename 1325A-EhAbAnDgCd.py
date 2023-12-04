import math

def lcm_gcd(n):
    a = 1
    b = n - 1
    while True:
        gcd = math.gcd(a, b)
        lcm = int((a * b) / gcd)
        if gcd + lcm == n:
            return [a, b]
        else:
            a += 1
            b -= 1
            
t = int(input())
total = []

for i in range(t):
    n = int(input())
    total.append(lcm_gcd(n))

for k in total:
    print(*k)