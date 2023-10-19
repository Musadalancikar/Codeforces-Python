
n, k = map(int, input().split())

yi = list(map(int, input().split()))

total = 0

for i in range(n):
    if (5 - yi[i]) >= k:
        total += 1

print(total // 3)

        