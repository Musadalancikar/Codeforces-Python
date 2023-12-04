def elevators(a, b, c):
    first_elevator = a-1
    second_elevator = 0
    if b < c:
        second_elevator += (c-b)
        second_elevator += (c-1)
    else:
        if c == 1:
            second_elevator += (b-c)
        else:
            second_elevator += (b-c)
            second_elevator += (c-1)
            
    if first_elevator == second_elevator:
        return 3
    elif first_elevator < second_elevator:
        return 1
    else:
        return 2
            
t = int(input())
total = []

for i in range(t):
    a, b, c = map(int, input().split())
    total.append(elevators(a, b, c))

for j in total:
    print(j)    