t = int(input())
result =  []

for i in range(t):
    n = int(input())
    if n % 4 == 0:
        result.append("YES")
    else:
        result.append("NO")
        
for j in result:
    print(j)