def solve(tests):
    res = 0
    pw = 1
    while pw <= tests:
        d = 1
        while d <= 9:
            if pw * d <= tests:
                res += 1
            d += 1
        pw = pw * 10 + 1
    return res


t = int(input())
total = []

for i in range(t):
    tests = int(input())
    total.append(solve(tests))   
    
for j in total:
    print(j)
    



