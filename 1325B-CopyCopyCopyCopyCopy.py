def copycopy(lst):
    return len(set(lst))

t = int(input())
result = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    result.append(copycopy(lst))

for k in result:
    print(k)