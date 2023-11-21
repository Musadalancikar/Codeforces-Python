def equal_coins(a,b,c,n):
    lst = [a,b,c]
    max_number = max(lst)
    result = 0
    for i in lst:
        result += abs((max_number) - i)
    
    if n >= result and (n - result) % 3 == 0:
        return "YES"
    else:
        return "NO"
    
t = int(input())
total = []
 
 
for i in range(t):
    a,b,c,n = list(map(int, input().split()))
    total.append(equal_coins(a,b,c,n))
 
for j in total:
    print(j)