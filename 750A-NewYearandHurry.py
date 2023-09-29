

n, m = list(map(int, input().split()))

total_time_dk = 4 * 60

min_time_dk = total_time_dk - m

total = 0
y = 0

for i in range(1, n+1):
    answer_time = 5
    x = answer_time * i
    y += x
    if min_time_dk - y >= 0:
        total += 1

print(total)