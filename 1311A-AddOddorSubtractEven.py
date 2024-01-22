def min_moves_to_obtain_b(a, b):
    if a == b:
        return 0
    elif (a > b and (a - b) % 2 == 0) or (a < b and (b - a) % 2 == 1):
        return 1
    else:
        return 2

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = min_moves_to_obtain_b(a, b)
    print(result)
