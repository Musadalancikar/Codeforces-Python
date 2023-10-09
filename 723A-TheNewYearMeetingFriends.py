

x1, x2, x3 = list(map(int, input().split()))

xtotal = [x1, x2, x3]

total = 0

y = sorted(xtotal)
total += abs(y[1] - y[0]) + abs(y[2] - y[1]) 

print(int(total))
