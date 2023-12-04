t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()

    if a[1] != a[2]:
        print("NO")
    else:
        print("YES")
        print(f"{a[0]} {a[0]} {a[2]}")
