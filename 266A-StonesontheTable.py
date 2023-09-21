n = int(input())
color = list(input())

sayac = 0

for i in range(n-1):
    if color[i] == color[i+1]:
        sayac += 1

print(sayac)