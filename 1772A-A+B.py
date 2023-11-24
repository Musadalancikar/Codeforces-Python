def sum_total(sum_lst):
    str_sum = sum_lst.split("+")
    int_sum = [int(x) for x in str_sum]
    return sum(int_sum)
            
t = int(input())
result = []

for i in range(t):
    sum_lst = input()
    result.append(sum_total(sum_lst))

for j in result:
    print(j)