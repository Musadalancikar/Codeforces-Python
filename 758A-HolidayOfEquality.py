

n = int(input())

k = list(map(int, input().split()))

max_k = max(k)

k.remove(max_k)

total = 0

for i in k:
    total += max_k - i
    
print(total)