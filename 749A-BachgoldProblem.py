def bachgold(n):
    if n % 2 == 0:
        x = int(n / 2)
        lst = [2] * x
        return lst
    else:
        x = int(n / 2) - 1
        if x >= 1:
            lst = [2] * x
            lst.insert(lst[-1], 3)
            return lst
        else:
            return [n]
    
n = int(input())

total = bachgold(n)

print(len(total))
print(*total)
