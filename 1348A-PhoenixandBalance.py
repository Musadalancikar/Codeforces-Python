def phoenix(n):
    lst = [2**j for j in range(1, n+1)]
    lst_1 = []
    lst_2 = []
    if len(lst) == 2:
        return abs(lst[0]-lst[-1])
    else:
        for k in range(int(len(lst)/2)):
            lst_1.append(lst[-1+k])
            
        for m in lst:
            if m not in lst_1:
                lst_2.append(m)
        
        return abs(sum(lst_1) - sum(lst_2))
    
t = int(input())
total = []

for i in range(t):
    n = int(input())
    total.append(phoenix(n))

for l in total:
    print(l)    