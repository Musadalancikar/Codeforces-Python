def find_secret_string(b):
    a = b[0] + b[1::2]
    return a

t = int(input())
for _ in range(t):
    b = input()
    a = find_secret_string(b)
    print(a)


