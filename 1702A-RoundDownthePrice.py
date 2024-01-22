def round_down_the_price(n):
    len_n = len(str(n))
    result = n - 10**(len_n-1)
    return result

t = int(input())

for i in range(t):
    n = int(input())
    print(round_down_the_price(n))