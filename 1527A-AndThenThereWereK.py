def find_maximum_k(n):
    k = n
    while (k & (k - 1)) != 0:
        k &= (k - 1)
    return k - 1

t = int(input())
for _ in range(t):
    n = int(input())
    result = find_maximum_k(n)
    print(result)
