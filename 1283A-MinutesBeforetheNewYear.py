def new_year_minutes(n):
    hour = 23 - n[0]
    minutes = 60 - n[1]
    
    if hour != 0:
        return int(hour*60) + minutes
    else:    
        return minutes 

t = int(input())
total = []

for i in range(t):
    n = list(map(int, input().split()))
    total.append(new_year_minutes(n))
    
for j in total:
    print(j)