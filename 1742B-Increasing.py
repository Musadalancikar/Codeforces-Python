def sortd(lst):
    if len(set(lst)) == 1 and len(lst) != 1:
        return "NO"
    
    elif len(set(lst)) != len(lst):
        return "NO"
    
    else:
        return "YES"
    
t = int(input())
total = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    total.append(sortd(lst))

for k in total:
    print(k)    