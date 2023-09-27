

n = int(input())
dolars_list = [100, 20, 10, 5, 1]
total = 0

while n > 0:
    for i in dolars_list:
        if n >= i:
            x = n // i
            total += x
            n = n % i
        
print(total)