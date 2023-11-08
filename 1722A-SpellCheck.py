def timur(n,name):
    name_timur = "Timur"
    name_timur = list(name_timur)
    input_name = list(name)
    if len(name_timur) == n:
        for j in name_timur:
            if j not in input_name:
                return "NO"
        return "YES"
    else:
        return "NO"
                
t = int(input())
total = []

for i in range(t):
    n = int(input())
    name = input()
    total.append(timur(n, name))

for l in total:
    print(l)