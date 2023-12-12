def elections(lst):
    max_lst = max(lst)
    if max_lst == 0:
        return [1, 1, 1]
    
    else:        
        total = []
        for j in lst:
            if j == max_lst and lst.count(j) > 1:
                total.append(1)
            elif j == max_lst and lst.count(j) ==1:
                total.append(0)
            else:
                total.append(max_lst - j + 1)
                
        return total

t = int(input())
result = []

for i in range(t):
    lst = list(map(int, input().split()))
    result.append(elections(lst))
    
for k in result:
    print(*k)