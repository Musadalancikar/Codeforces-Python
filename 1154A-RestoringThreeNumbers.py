
x1, x2, x3, x4 = list(map(int, input().split()))

sum_list = [x1, x2, x3, x4]

max_sm = max(sum_list)

sum_list.remove(max_sm)

numbers = []

for i in range(len(sum_list)):
    for j in range(i+1, len(sum_list)):    
        numbers.append((sum_list[i] + sum_list[j]) - max_sm)
        
print(*numbers)
        

        
        