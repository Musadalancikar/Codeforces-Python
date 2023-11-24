def fafa_company(t):
    lst = [x for x in range(1, t) if t % x == 0]
    return len(lst)

t = int(input())
print(fafa_company(t))