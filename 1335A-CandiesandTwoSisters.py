

n = int(input())

total_score = []

for i in range(n):
    x = int(input())
    if x % 2 == 0:
        total = int(x / 2) - 1
        total_score.append(total)
        
    else:
        total = int(x / 2)
        total_score.append(total)
        
for j in total_score:
    print(j)