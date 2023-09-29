
n = int(input())

point_list = list(map(int, input().split()))

total = 0

max_point = point_list[0]
min_point = point_list[0]

for i in point_list:
    if i > max_point:
        max_point = i
        total += 1
        
    elif i < min_point:
        min_point = i
        total += 1
        
    else:
        total = total
        
print(total)