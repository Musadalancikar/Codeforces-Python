

t = int(input())
result = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    e = []
    o = []
    for j in range(n):
        if j % 2 == 0:
            if j % 2 != lst[j] % 2:
                e.append(lst[j])
        else:
            if j % 2 != lst[j] % 2:
                o.append(lst[j])
    
    if len(e) == len(o):
        result.append(len(o))
    elif len(e) == 0 and len(o) == 0:
        result.append(0)
    else:
        result.append(-1)
    
for k in result:
    print(k)