

t = int(input())

result = []

for i in range(t):
    x = int(input())
    if x <= 1399:
        result.append("Division 4")
        
    elif x >= 1400 and x <= 1599:
        result.append("Division 3")
        
    elif x >= 1600 and x <= 1899:
        result.append("Division 2")
        
    else:
        result.append("Division 1")
        
for j in result:
    print(j)
        
