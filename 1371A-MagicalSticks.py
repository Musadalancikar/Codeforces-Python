import math

def max_equal_sticks(n):
    return math.ceil(n / 2)

t = int(input())
total_result = []

for i in range(t):
    n = int(input())
    total_result.append(max_equal_sticks(n))

for k in total_result:
    print(k)