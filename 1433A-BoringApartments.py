def len_total(x):
    total = 0 
    for i in range(1, x+1):
        total += i 
    return total
 
def sum_total(number):
    x = len(number)
    y = int(number[0])
    return (y-1)*10 + len_total(x)
    
t = int(input())
total_result = []
 
for j in range(t):
    number = input()
    total_result.append(sum_total(number))
 
for k in total_result:
    print(k)