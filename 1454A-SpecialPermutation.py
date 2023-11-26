def permütation(n):
    number_list = [x for x in range(1,n+1)]
    copy_list = number_list.copy()
    if n % 2 == 0:
        for j in range(0, n, 2):
            number_list[j] = copy_list[j+1]
            number_list[j+1] = copy_list[j]
        
        return number_list
    else:
        for k in range(0, n-1):
            number_list[k] = copy_list[k+1]

        number_list[-1] = copy_list[0]
        return number_list            

t = int(input())
total = []

for i in range(t):
    n = int(input())
    total.append(permütation(n))
    
for l in total:
    print(*l)