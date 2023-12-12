def pi_count(n):
    pi_number = "314159265358979323846264338327"
    total = 0
    for j in range(len(n)):
        if n[j] == pi_number[j]:
            total += 1
        else:
            break
    return total

t = int(input())
result = []

for i in range(t):
    n = input()
    result.append(pi_count(n))

for k in result:
    print(k)    