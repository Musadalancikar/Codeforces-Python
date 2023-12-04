def good_kid(lst):
    result = 1
    lst[lst.index(min(lst))] += 1
    for j in lst:
        result *= j
        
    return result

t = int(input())
total = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split())) 
    total.append(good_kid(lst))

for k in total:
    print(k)