m, n = list(map(int, input().split()))

x = []
y = []

for i in range(1, m+1):
    for j in range(1, n+1):
        x.append([i,j])
        
    y.append(x)
    x = []
    
total = 0
for k in range(1, len(y)+1):
    if k % 2 != 0:
        for l in y[k-1]:
            l.clear()
            l.append("#")
    elif k % 2 == 0:
        if total % 2 == 0:
            for p in y[k-1]:
                p.clear()
                p.append(".")
            y[k-1][-1] = ["#"]
            total += 1
        else:
            for r in y[k-1]:
                r.clear()
                r.append(".")
            y[k-1][0] = ["#"]
            total += 1

sa = []
sa1 = []

for i in y:
    for j in i:
        z = *j,
        sa.append(z[0])
    sa1.append(sa)
    sa = []
    
for i in sa1:
    print("".join(i))        