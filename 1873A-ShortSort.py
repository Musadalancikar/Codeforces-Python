def sort_n(n):
    total = 0
    n_true = "abc"
    for j in range(len(n_true)):
        if n_true[j] != n[j]:
            total += 1
        
    if total <= 2:
        return "YES"
    else:
        return "NO"

t = int(input())
result = []

for i in range(t):
    n = input()
    result.append(sort_n(n))

for k in result:
    print(k)

