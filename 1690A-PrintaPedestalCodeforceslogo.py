def print_a_pedestal(n):
    if n % 3 == 0:
        h1 = n // 3
        h2 = h1 + 1
        if h1 + h2 >= n:
            h1 -= 1 
            h3 = n - h1 - h2
            return [h1, h2, h3]
        else:
            h3 = n - h1 - h2
            return [h1, h2, h3]
    else:
        h1 = n // 3 + 1
        h2 = h1 + 1
        if h1 + h2 >= n:
            h1 -= 1
            h3 = n - h1 - h2
            return [h1, h2, h3]
        else:
            h3 = n - h1 - h2
            return [h1, h2, h3]
        
t = int(input())

for i in range(t):
    n = int(input())
    print(*print_a_pedestal(n))