def permütation(n):
    if n % 2 == 1:
        return [-1]
    else:
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

n = int(input())
print(*permütation(n))
    
