def cut_total(w,h,n):
    total = 0
    
    if w % 2 == 1 and h % 2 == 1 and n == 1:
        return "YES"
    else:
        while True:
            if w % 2 == 0:
                w = int(w / 2)
                total += 1
            elif h % 2 == 0:
                h = int(h / 2)
                total += 1
            else:
                break
            
        if 2 ** total >= n:
            return "YES"
        else:
            return "NO"

t = int(input())
result = []

for i in range(t):
    w, h, n = map(int, input().split())
    result.append(cut_total(w, h, n))
    
for k in result:
    print(k)

