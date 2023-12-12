def x_y_z(a, b, c, d):
    x = b
    y = c
    z = c
    return [x, y, z]


t = int(input())
result = []

for i in range(t):
    a, b, c, d = map(int, input().split())
    result.append(x_y_z(a, b, c, d))

for j in result:
    print(*j)