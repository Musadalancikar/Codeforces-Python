def max_cubes(x):
    total_sum = 0
    for i in range(1,x+1):
        total_sum += int((i*(i+1))/2)
    return total_sum

t = int(input())

x = 1
while True:
    if max_cubes(x) > t:
        print(x-1)
        break 
    else:
        x += 1
                


