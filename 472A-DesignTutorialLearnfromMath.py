n = int(input())

def compite(x):
    total = 0
    for j in range(1,x+1):
        if x % j == 0:
            total += 1
            if total > 2:
                return x
                break
        else:
            total = total
        
    return total

total1 = []

if n % 2 == 0:
    a = int(n / 2)
    if compite(a) == a:
        total1.append([a,a])
    else:
        a = int(n/2) + 1
        while True:
            if compite(a) == a:
                b = n - a
                if compite(b) == b:
                    total1.append([a,b])
                    break
                else:
                    a += 1
            else:
                a += 1
        
else:
    c = int(n/2) + 1
    while True:
        if compite(c) == c:
            d = n - c
            if compite(d) == d:
                total1.append([c,d])
                break
            else:
                c += 1
        else:
            c += 1

for i in total1:
    print(*i)
                    
                
        