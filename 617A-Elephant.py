n = int(input())

total = 0

for i in range(1,6):
    if n >= 6-i:
        x = n // (6-i)
        total += x
        n = n - (x*(6-i))
        if n == 0:
            print(total)
        