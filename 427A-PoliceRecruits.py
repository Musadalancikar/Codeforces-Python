n = int(input())

police_list = list(map(int, input().split()))

police_total = 0
crimers_total = 0

for i in range(n):
    if police_list[i] == -1:
        if police_total == 0:
            crimers_total += 1
        else:
            police_total -= 1
            crimers_total = crimers_total
            
    else:
        police_total += police_list[i]
        
print(crimers_total)