def codeforces_name(n):
    x = "codeforces"
    total = 0
    for j in range(len(n)):
        if n[j] != x[j]:
            total += 1
    return total

t = int(input())
result = []

for i in range(t):
    n = input()
    result.append(codeforces_name(n))
    
for k in result:
    print(k)