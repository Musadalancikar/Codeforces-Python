def sasha_and_array_coloring(n, lst):
    if n == 1:
        return 0
    elif n % 2 == 1:
        total = 0
        for i in range(n//2):
            total += (max(lst) - min(lst))
            lst.remove(max(lst))    
            lst.remove(min(lst))
        return total
    else:
        total = 0
        for i in range(n//2):
            total += (max(lst) - min(lst))
            lst.remove(max(lst))    
            lst.remove(min(lst))
        return total

t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    print(sasha_and_array_coloring(n, lst))    