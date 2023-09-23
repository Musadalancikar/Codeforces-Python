
n, k = list(map(int, input().split()))

height_list = list(map(int, input().split()))

total = 0

for i in height_list:
    if i <= k:
        total += 1
        
    else:
        total += 2
        
print(total)
    
    