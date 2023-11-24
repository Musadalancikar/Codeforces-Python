t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0
    
    numbers = list(map(int, input().split()))
    
    for x in numbers:
        if x % 2 == 0:
            cnt += 1
    
    if cnt == n:
        print("Yes")
    else:
        print("No")
