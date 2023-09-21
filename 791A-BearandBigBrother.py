a, b = list(map(int, input().split()))

sayac = 0

while True:
    if a <= b:
        a = a * 3
        b = b *2
        sayac += 1
    else:
        print(sayac)
        break
