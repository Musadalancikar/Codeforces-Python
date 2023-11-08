def floor_number(n,x):
    first_floor = 2
    y = 1
    while True:
        if n > 2:
            if (x*y) + first_floor >= n:
                return y+1
                break
            else:
                y += 1
        else:
            return 1
            break
        
t = int(input())
total = []

for i in range(t):
    n,x = list(map(int, input().split()))
    total.append(floor_number(n, x))
                 
for j in total:
    print(j)