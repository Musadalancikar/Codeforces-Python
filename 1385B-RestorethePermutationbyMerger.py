def restore_permü(lst):
    result = []
    for j in lst:
        if j not in result:
            result.append(j)
    return result

t = int(input())
total = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    total.append(restore_permü(lst))

for k in total:
    print(*k)