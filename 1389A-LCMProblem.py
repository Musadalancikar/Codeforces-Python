def lcm(l,r):
    if l * 2 > r:
        return [-1, -1]
    else:
        return [l, l * 2]
        
t = int(input())
total = []

for i in range(t):
    l, r = map(int, input().split())
    total.append(lcm(l, r))
    
for k in total:
    print(*k)

