

n = int(input())

match_list = []

for i in range(n):
    x = list(input().split())
    match_list.append(x)

home_owner = []
away = []

for i in match_list:
    home_owner.append([i[0]])

for i in match_list:
    away.append([i[1]])

total = 0

for i in home_owner:
    for j in away:
        if i == j:
            total += 1
            
print(total)