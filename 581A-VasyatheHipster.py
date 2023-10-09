

r, b = list(map(int, input().split()))
total1 = 0
total2 = 0
while r >= 0 or b >= 0:
    if r > 0 and b > 0:
        total1 += 1
        r -= 1
        b -= 1
    else:
        total2 += r // 2 
        total2 += b // 2
        break
    
print(*[total1, total2])

        