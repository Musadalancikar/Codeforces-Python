string = "codeforces"

t = int(input())

result = []

for i in range(t):
    s = input()
    if s in string:
        result.append("YES")
    else:
        result.append("NO")
        
for j in result:
    print(j)