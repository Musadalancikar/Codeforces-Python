def is_same(n, rgb1, rgb2):
    new_rgb1 = rgb1.replace("G", "B")
    new_rgb2 = rgb2.replace("G", "B")
    total = 0
    for j in range(n):
        if new_rgb1[j] == new_rgb2[j]:
            total += 1
    
    if total == n:
        return "YES"
    else:
        return "NO"

t = int(input())
result = []

for i in range(t):
    n = int(input())
    rgb1 = input()
    rgb2 = input()
    result.append(is_same(n, rgb1, rgb2))
    
for l in result:
    print(l)