def plus_or_minus(lst):
    x = lst[:2]
    if sum(x) == lst[-1]:
        return "+"
    else:
        return "-"
 
t = int(input())
total_result = []
 
for i in range(t):
    lst = list(map(int, input().split()))
    total_result.append(plus_or_minus(lst))
 
for j in total_result:
    print(j)
    