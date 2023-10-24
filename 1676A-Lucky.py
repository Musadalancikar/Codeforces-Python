
t = int(input())

result = []

for i in range(t):
    x = list(input())
    first = x[:3]
    last = x[-3:]
    if sum([int(i) for i in first]) == sum([int(i) for i in last]):
        result.append("YES")
        
    else:
        result.append("NO")

for i in result:
    print(i)