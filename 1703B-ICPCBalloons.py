def team_point(team):
    result = 0
    st_len = len(set(team))
    result += ((st_len*2) + (n - st_len))
    return result 
    
t = int(input())
total = []

for i in range(t):
    n = int(input())
    team = input()
    total.append(team_point(team))
    
for k in total:
    print(k)
